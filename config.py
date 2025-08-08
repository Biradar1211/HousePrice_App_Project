from pymongo import MongoClient

Mongo_URl = "mongodb://localhost:27017/"
DB_NAME = "house"
COLLECTION_NAME = "rent"

client = MongoClient(Mongo_URl)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

