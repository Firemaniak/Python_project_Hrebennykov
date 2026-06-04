# User Selection Module

from logger import log_search, get_popular_searches
from animation import loading_animation
from sql_requests import (
    select_category,
    search_films,
    get_all_categories,
    get_year_range,
    search_by_year_range,
)

#---------------------------------------# user should select option-----------------------------------------------------

def select_options() -> bool:

    """
    Handle the user's main menu choice.

    Returns:
        bool: True if the application should continue running,
        False if the user chooses to exit.
    """

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

#---------------------------------------------------# Keyword Search----------------------------------------------------

def handle_keyword_search() -> None:

    """
    Search movies by title keyword
    and save the selected movie to statistics.
    """

    keyword = input("Enter a film name: ")
    loading_animation()
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


#-------------------------------------------------# Search by Category--------------------------------------------------

def handle_category_search() -> None:

    """
    Display movie categories and allow
    browsing movies by selected category.
    """

    loading_animation()

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
            loading_animation()
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

#-----------------------------------------------------# Search by Year--------------------------------------------------

def handle_year_search() -> None:

    """
    Search movies by a selected release year range.
    """

    min_year, max_year = get_year_range()

    print(f"Available years: {min_year} - {max_year}")

    start_year = input("Enter start year: ")
    end_year = input("Enter end year: ")
    loading_animation()

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

#---------------------------------------------------# Displaying Popular Queries----------------------------------------

def handle_popular_searches() -> None:

    """
    Display the most popular movie searches
    stored in MongoDB.
    """

    loading_animation()

    popular_movies = list(get_popular_searches())

    if not popular_movies:
        print("\nNo search statistics yet.")
        return

    print("\nPopular searches:\n")

    for i, movie in enumerate(popular_movies, start=1):
        print(f"{i}. {movie['_id']} ({movie['count']} searches)")

#-----------------------------------------------------------------------------------------------------------------------

