#Модуль чисто для подключения к базе данных MY_SQL

import pymysql

from settings import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE,
    MYSQL_PORT
)

#-----------------------------------------------------------------------------------------------------------------------

def get_connection():
    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT
    )
    return connection

#-----------------------------------------------------------------------------------------------------------------------