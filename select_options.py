from logger import log_search, get_popular_searches
from sql_requests import (
    select_category,
    search_films,
    get_all_categories,
    get_year_range,
    search_by_year_range,
)


#---------------------------------------# user should select option-----------------------------------------------------

def select_options():
    choice = input("Choose an option: ")

    if choice == "1":
        handle_keyword_search()

    elif choice == "2":
        handle_category_search()

    elif choice == "3":
        handle_year_search()

    elif choice == "4":
        handle_popular_searches()

    elif choice == "0":
        print("Goodbye!")
        return False

    else:
        print("Invalid option.")

    return True

#---------------------------------------------------# Поиска по ключевому слову-----------------------------------------

def handle_keyword_search():
    keyword = input("Enter a film name: ")
    films = search_films(keyword)

    if not films:
        print("No movies found.")
        return

    for i, row in enumerate(films, start=1):
        print(f"{i}. {row[0]}")

    if len(films) == 1:
        movie_title = films[0][0]

        log_search(movie_title)
        print(f"Film: {movie_title} --> Movie search saved.")
        return

    try:
        film_number = int(
            input("Choose movie number to save search: ")
        )

        selected_movie = films[film_number - 1]
        movie_title = selected_movie[0]

        log_search(movie_title)

        print(f"Film: {movie_title} --> Movie search saved.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    except IndexError:
        print("Invalid movie number.")


#-------------------------------------------------# Поиска по категориях------------------------------------------------

def handle_category_search():

    while True:
        categories = get_all_categories()

        print("\nAvailable categories:\n")

        for row in categories:
            print(f"{row[0]}. {row[1]}")

        category_id = input(
            "\nChoose number of category "
            "(or enter 0 to return to main menu): "
        )

        if category_id == "0":
            break

        if not category_id.isdigit():
            print("\nInvalid category. Please enter a number.")
            continue

        category_ids = [str(row[0]) for row in categories]

        if category_id not in category_ids:
            print("\nCategory does not exist.")
            continue

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


#-----------------------------------------------------# Поиска по годам-------------------------------------------------

def handle_year_search():

    min_year, max_year = get_year_range()

    print(f"Available years: {min_year} - {max_year}")

    start_year = input("Enter start year: ")
    end_year = input("Enter end year: ")

    if not start_year.isdigit() or not end_year.isdigit():
        print("Years must be numbers.")
        return

    start_year = int(start_year)
    end_year = int(end_year)

    if start_year > end_year:
        print("Start year cannot be greater than end year.")
        return

    if start_year < min_year or end_year > max_year:
        print(
            f"Years must be between "
            f"{min_year} and {max_year}."
        )
        return

    offset = 0
    limit = 15

    while True:

        movies = search_by_year_range(
            start_year,
            end_year,
            limit,
            offset
        )

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

#---------------------------------------------------# Вывод популярных запросов-----------------------------------------

def handle_popular_searches():

    popular_movies = list(get_popular_searches())

    if not popular_movies:
        print("\nNo search statistics yet.")
        return

    print("\nPopular searches:\n")

    for i, movie in enumerate(popular_movies, start=1):
        print(f"{i}. {movie['_id']} ({movie['count']} searches)")
#

#-----------------------------------------------------------------------------------------------------------------------

