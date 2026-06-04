# Логика для вызова запроса с sql_queries


from sql_queries import (
    SEARCH_FILMS,
    GET_ALL_CATEGORIES,
    SELECT_CATEGORY,
    SEARCH_BY_YEAR_RANGE,
    GET_YEAR_RANGE,
)

from db_decorators import with_connection

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска фильмов по ключ слову

@with_connection
def search_films(connection, keyword):

    with connection.cursor() as cursor:

        cursor.execute(
            SEARCH_FILMS,
            (f"%{keyword}%",)
        )

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска по жанрам

@with_connection
def get_all_categories(connection):

    with connection.cursor() as cursor:

        cursor.execute(GET_ALL_CATEGORIES)

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

#Функция для вывода фильмов по выбр категории

@with_connection
def select_category(connection, category_id, limit=15, offset=0):

    with connection.cursor() as cursor:

        cursor.execute(
            SELECT_CATEGORY,
            (category_id, limit, offset)
        )

        return cursor.fetchall()

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска фильмов по выбору года выпуска или диапазона годов

@with_connection
def search_by_year_range(
    connection,
    start_year,
    end_year,
    limit=15,
    offset=0
):

    with connection.cursor() as cursor:

        cursor.execute(
            SEARCH_BY_YEAR_RANGE,
            (start_year, end_year, limit, offset)
        )

        return cursor.fetchall()

# И так же функция для просмотра доступных годов

@with_connection
def get_year_range(connection):

    with connection.cursor() as cursor:

        cursor.execute(GET_YEAR_RANGE)

        return cursor.fetchone()

#-----------------------------------------------------------------------------------------------------------------------