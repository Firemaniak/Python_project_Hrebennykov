# Декоратор для работы с соединением

from functools import wraps

from my_sql_client import get_connection


def with_connection(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        connection = get_connection()

        try:
            return func(connection, *args, **kwargs)

        finally:
            connection.close()

    return wrapper