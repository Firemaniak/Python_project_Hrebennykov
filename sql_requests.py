# Logic for executing a query from `sql_queries`


from sql_queries import (
    SEARCH_FILMS,
    GET_ALL_CATEGORIES,
    SELECT_CATEGORY,
    SEARCH_BY_YEAR_RANGE,
    GET_YEAR_RANGE,
)

from db_decorators import with_connection

#-----------------------------------------------------------------------------------------------------------------------

@with_connection
def search_films(connection, keyword: str):

    """
    Search movies by title keyword.
    """

    with connection.cursor() as cursor:
        cursor.execute(
            SEARCH_FILMS,
            (f"%{keyword}%",)
        )

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

@with_connection
def get_all_categories(connection):

    """
    Return all available movie categories.
    """

    with connection.cursor() as cursor:
        cursor.execute(GET_ALL_CATEGORIES)

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

# Function for displaying movies by selected category

@with_connection
def select_category(connection, category_id: str, limit: int = 15, offset: int = 0):

    """
    Return movies by selected category with pagination.
    """

    with connection.cursor() as cursor:
        cursor.execute(
            SELECT_CATEGORY,
            (category_id, limit, offset)
        )

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

# Function for searching for movies by selected release year or year range

@with_connection
def search_by_year_range(
    connection,
    start_year: int,
    end_year: int,
    limit: int = 15,
    offset: int = 0
):

    """
    Return movies within the selected release year range.
    """

    with connection.cursor() as cursor:
        cursor.execute(
            SEARCH_BY_YEAR_RANGE,
            (start_year, end_year, limit, offset)
        )

        return cursor.fetchall()

#------------- Function for viewing available years

@with_connection
def get_year_range(connection):

    """
    Return the minimum and maximum movie release years.
    """

    with connection.cursor() as cursor:
        cursor.execute(GET_YEAR_RANGE)

        return cursor.fetchone()

#-----------------------------------------------------------------------------------------------------------------------