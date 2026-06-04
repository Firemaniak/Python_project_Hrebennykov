# Для логирования популярных запросов

from pymongo.errors import PyMongoError

from mongo_client import get_collection


def log_search(movie_title):

    if not movie_title:
        return

    try:
        collection = get_collection()

        collection.insert_one({
            "movie_title": movie_title
        })

    except PyMongoError:
        print("Could not save search statistics.")


def get_popular_searches():

    try:
        collection = get_collection()

        return collection.aggregate([
            {
                "$group": {
                    "_id": "$movie_title",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {"count": -1}
            },
            {
                "$limit": 10
            }
        ])

    except PyMongoError:
        print("Could not load popular searches.")
        return []