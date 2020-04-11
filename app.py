import os
import pymongo
from flask import Flask
from os import path
if path.exists("env.py"):
    import env

MONGO_URI=os.environ.get("MONGO_URI")
DBS_NAME="topTenDB"
COLLECTION_NAME="categories"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Wiihoo, Mongo is connected!")
        return conn
    except pymongo.error.ConnectionFailure as e:
        print("Could not connect %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()


for doc in documents:
    print(doc)
