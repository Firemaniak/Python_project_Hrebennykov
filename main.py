import ui_module

from settings import MYSQL_HOST

from sql_requests import (
    get_all_films,
    select_category,
    search_films,
    get_all_categories,
    get_year_range,
    search_by_year_range
)

# -----------------------------------------------------------------------------------------------------------------------

# print(get_all_films())
# print(MYSQL_HOST)

# -----------------------------------------------------------------------------------------------------------------------

def main():
    ui_module.show_welcome()

    while True:
        ui_module.show_menu()

        result = select_options()

        if result is False:
            break


# -----------------------------------------------------------------------------------------------------------------------

def select_options():
    choice = input("Choose an option: ")

    if choice == "1":                             # Поиска по ключевому слову
        keyword = input('Enter a film name: ')
        films = search_films(keyword)
        for i, row in enumerate(films, start=1):
            print(f'{i}. {row[0]}')


    elif choice == "2":                           # Поиска по категориях

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



    elif choice == "3":                                   # Поиска по годам

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

    elif choice == "4":                                          # Популярные запросы
        pass

    elif choice == "0":                                          # Выход из консольного приложения
        print("Goodbye!")
        return False


# -----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------------------------------------------------