from datetime import datetime

from pymongo import MongoClient

client = MongoClient('<YOUR_ATLAS_DATA_LAKE_URI>')
db = client.get_database("test")
coll = db.get_collection("orders")

start_date = datetime(2020, 5, 1, 0, 0, 0)  # May 1st
end_date = datetime(2020, 6, 1, 0, 0, 0)  # June 1st

pipeline = [
    {
        '$match': {
            'created': {
                '$gte': start_date,
                '$lt': end_date
            }
        }
    },
    {
        '$out': {
            's3': {
                'bucket': 'cold-data-mongodb',
                'region': 'eu-west-1',
                'filename': start_date.isoformat('T', 'milliseconds') + 'Z-' + end_date.isoformat('T', 'milliseconds') + 'Z',
                'format': {'name': 'json', 'maxFileSize': "200MiB"}
            }
        }
    }
]

coll.aggregate(pipeline)
print('Archive created!')
