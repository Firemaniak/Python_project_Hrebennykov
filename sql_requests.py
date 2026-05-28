#В виде констант храним запросы

from my_sql_client import get_connection

#-----------------------------------------------------------------------------------------------------------------------

#Функция для вывода всех фильмов
def get_all_films():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT film_id, title FROM film")
        results = cursor.fetchall()
    connection.close()
    return results

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска фильмов по ключ слову
def search_films(keyword):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT title FROM film WHERE title LIKE %s LIMIT 10",
                       (f"%{keyword}%",)
                       )
        results = cursor.fetchall()
    connection.close()
    return results

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска по жанрам
def get_all_categories():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT category_id, name
            FROM category
            ORDER BY name
        """)

        results = cursor.fetchall()

    connection.close()
    return results

#-----------------------------------------------------------------------------------------------------------------------

#Функция для вывода фильмов по выбр категории

def select_category(category_id, limit=15, offset=0):
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT f.title
            FROM film AS f
            JOIN film_category AS fc
                ON f.film_id = fc.film_id
            WHERE fc.category_id = %s
            ORDER BY f.title
            LIMIT %s OFFSET %s
        """, (category_id, limit, offset))

        movies = cursor.fetchall()

    connection.close()
    return movies

#-----------------------------------------------------------------------------------------------------------------------

#Функция для поиска фильмов по выбору года выпуска или диапазона годов

def search_by_year_range(start_year, end_year, limit=15, offset=0):
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT title, release_year
            FROM film
            WHERE release_year BETWEEN %s AND %s
            ORDER BY release_year, title
            LIMIT %s OFFSET %s
        """, (start_year, end_year, limit, offset))

        movies = cursor.fetchall()

    connection.close()
    return movies

# И так же функция для просмотра доступных годов

def get_year_range():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT MIN(release_year), MAX(release_year)
            FROM film
        """)

        year_range = cursor.fetchone()

    connection.close()
    return year_range

#-----------------------------------------------------------------------------------------------------------------------