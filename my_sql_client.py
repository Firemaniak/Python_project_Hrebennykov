# Module for connecting to a MySQL database

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

    """
    Create and return a connection
    to the MySQL Sakila database.
    """

    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT
    )
    return connection

#-----------------------------------------------------------------------------------------------------------------------