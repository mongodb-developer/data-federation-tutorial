# Data Federation Tutorial

This repo contains some code samples for a DevCenter blog post: 

- [MongoDB Atlas Data Federation Tutorial: Federated Queries and $out to AWS S3](http://developer.mongodb.com/how-to/atlas-data-lake-federated-queries-out-aws-s3)

# Requirements

- Python 3
- install required libs: `pip3 install -r requirements.txt`

# Run

- For `archive.py` and `federated_queries.py` you will need the URI of your federated instance.
- For `insert.py` and `remove.py` you will need your MongoDB Atlas URI.

## insert.py

Inserts documents in `test.orders` of the specified MongoDB cluster.

## archive.py

This script uses the new $out stage in order to archive docs from our Atlas cluster to a S3 JSON file.

## remove.py

Removes the documents that we have archived.

## federated_queries.py

This script checks that we can still access 100% of the data using the federated instance.
