# Для логирования популярных запросов

from mongo_client import get_collection

collection = get_collection()


def log_search(movie_title):

    if movie_title is None:
        return

    collection = get_collection()

    collection.insert_one({
        "movie_title": movie_title
    })

#-----------------------------------------------------------------------------------------------------------------------
# Чтение данных из MongoDB

def get_popular_searches():
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