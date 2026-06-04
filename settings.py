# Intermediary for connecting to the database

import os
from dotenv import load_dotenv

#-----------------------------------------------------------------------------------------------------------------------
# Get data to connect to SQL

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))

#-----------------------------------------------------------------------------------------------------------------------
# Get URL connect to MongoAtlas

MONGO_URI = os.getenv("MONGO_URI")