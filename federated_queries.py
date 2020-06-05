from pymongo import MongoClient

client = MongoClient('<YOUR_ATLAS_DATA_LAKE_URI>')
db = client.get_database("test")
coll = db.get_collection("orders")

print("All the docs from S3 + Atlas:")
docs = coll.find()
for d in docs:
    print(d)

pipeline = [
    {
        '$group': {
            '_id': None,
            'total': {
                '$sum': '$price'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
]

print('\nI can also run an aggregation:')
print(coll.aggregate(pipeline).next())
