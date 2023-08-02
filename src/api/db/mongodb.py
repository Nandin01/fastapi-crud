from typing import Collection

from pymongo import MongoClient
from pymongo.database import Database

MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
MONGO_DB_NAME = "todo"

client = MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]

def get_database() -> Database:
    return db

def get_todos_collection() -> Collection:
    return db["todos"]
