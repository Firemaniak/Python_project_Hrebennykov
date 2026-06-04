# Working with MongoDB Atlas

from pymongo import MongoClient
from settings import MONGO_URI

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)

db = client["movie_search_app"]

collection = db["search_logs"]


def get_collection():

    """
    Return the MongoDB collection used
    for storing movie search statistics.
    """

    return collection