# Working with MongoDB Atlas

from pymongo import MongoClient
from settings import MONGO_URI


def get_collection():
    client = MongoClient(MONGO_URI)
    db = client["movie_search_app"]
    return db["search_logs"]