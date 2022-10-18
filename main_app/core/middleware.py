from pymongo import MongoClient
import os

# establish a connection to MongoDB


def connect_db():

    client = MongoClient(os.environ.get('MONGODB_URI'))

    return client
