"""
Create a database instance using credentials that will be used to access database.
"""
from pymongo import MongoClient
import constants

mongo = MongoClient(**constants.mongo_creds)
db = mongo.web
