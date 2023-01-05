from datetime import datetime
from pymongo import MongoClient

client = MongoClient('<YOUR_ATLAS_URI>')
db = client.get_database('test')
coll = db.get_collection('orders')

start_date = datetime(2020, 5, 1)  # May 1st
end_date = datetime(2020, 6, 1)  # June 1st
query = {
    'created': {
        '$gte': start_date,
        '$lt': end_date
    }
}

result = coll.delete_many(query)
print('Deleted', result.deleted_count, 'orders.')
