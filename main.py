import ui_module

from settings import MYSQL_HOST
from logger import log_search, get_popular_searches
from sql_requests import (
    get_all_films,
    select_category,
    search_films,
    get_all_categories,
    get_year_range,
    search_by_year_range
)

# -----------------------------------------------------------------------------------------------------------------------

def main():
    ui_module.show_welcome()

    is_running = True

    while is_running:
        ui_module.show_menu()
        is_running = select_options()


# -----------------------------------------------------------------------------------------------------------------------
# Выбор опций для пользователя

def select_options():
    choice = input("Choose an option: ")


    if choice == "1":                               # Поиска по ключевому слову-----------------------------------------
        keyword = input("Enter a film name: ")
        films = search_films(keyword)

        for i, row in enumerate(films, start=1):
            print(f"{i}. {row[0]}")

        if len(films) == 1:
            log_search(films[0][0])
            print(f"Film: {films[0][0]} --> Movie search saved.")

        elif len(films) >= 2:

            film_number = input("Choose movie number to save search: ")

            selected_movie = films[int(film_number) - 1]

            log_search(selected_movie[0])

            print(f"Film: {selected_movie[0]} --> Movie search saved.")




    elif choice == "2":                           # Поиска по категориях------------------------------------------------

        while True:

            categories = get_all_categories()

            print("\nAvailable categories:\n")

            for row in categories:
                print(f'{row[0]}. {row[1]}')

            category_id = input(

                "\nChoose number of category "

                "(or enter 0 to return to main menu): "

            )

            if category_id == "0":
                break

            offset = 0

            limit = 15

            while True:

                movies = select_category(category_id, limit, offset)

                if not movies:
                    print("\nNo more movies.")

                    break

                print("\nMovies:\n")

                for i, row in enumerate(movies, start=offset + 1):
                    print(f"{i}. {row[0]}")

                action = input(

                    "\n1 - next 15 movies\n"

                    "0 - back to categories\n"

                    "Choose option: "

                )

                if action == "1":

                    offset += limit


                elif action == "0":

                    break


                else:

                    print("\nInvalid option.")

                    break




    elif choice == "3":                                   # Поиска по годам----------------------------------------------

        min_year, max_year = get_year_range()

        print(f"Available years: {min_year} - {max_year}")

        start_year = input("Enter start year: ")

        end_year = input("Enter end year: ")

        offset = 0

        limit = 15

        while True:

            movies = search_by_year_range(start_year, end_year, limit, offset)

            if not movies:
                print("\nNo more movies.")

                break

            for i, row in enumerate(movies, start=offset + 1):
                print(f"{i}. {row[0]} ({row[1]})")

            action = input(

                "\nEnter 1 to show next 15 movies, "

                "or 0 to return to main menu: "

            )

            if action == "1":

                offset += limit


            elif action == "0":

                break


            else:

                print("Invalid option.")

                break



    elif choice == "4":                                         # Вывод популярных запросов-----------------------------

        popular_movies = get_popular_searches()

        print("\nPopular searches:\n")

        for i, movie in enumerate(popular_movies, start=1):
            print(f"{i}. {movie['_id']} ({movie['count']} searches)")
            return True

    elif choice == "0":                                          # Выход из консольного приложения----------------------
        print("Goodbye!")
        return False

    return True

# -----------------------------------------------------------------------------------------------------------------------
# Вызов только с главного модуля(тут)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------

