from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.json_util import dumps
def getAllproducts():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    mydb=client['store']
    collection = mydb ['shampoo']
    productinfo = collection.find()
    return dumps(productinfo)