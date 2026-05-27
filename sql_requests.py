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
            SELECT name
            FROM category
            ORDER BY name
        """)

        results = cursor.fetchall()

    connection.close()
    return results

#-----------------------------------------------------------------------------------------------------------------------