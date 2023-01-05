from pymongo import MongoClient
from datetime import datetime

client = MongoClient('YOUR_ATLAS_URI')
db = client.get_database('test')
coll = db.get_collection('orders')

orders = [
    {
        "_id": 1,
        "created": datetime(2020, 5, 30), # May 30th
        "items": [1, 3],
        "price": 20
    },
    {
        "_id": 2,
        "created": datetime(2020, 5, 31), # May 31st
        "items": [2, 3],
        "price": 25
    },
    {
        "_id": 3,
        "created": datetime(2020, 6, 1), # June 1st
        "items": [1, 3],
        "price": 20
    },
    {
        "_id": 4,
        "created": datetime(2020, 6, 2), # June 2nd
        "items": [1, 2],
        "price": 15
    },
]

coll.insert_many(orders)
