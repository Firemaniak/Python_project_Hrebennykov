from mongo_client import get_collection

collection = get_collection()

collection.insert_one({
    "test": "hello mongo"
})

print("Connected!")