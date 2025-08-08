from config import collection

def insert_prediction(data: dict):
    collection.insert_one(data)
