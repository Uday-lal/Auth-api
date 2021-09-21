from pymongo import MongoClient
import urllib.parse
import json
import os

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "config.json"), "r")
data = json.load(file)
username = data["username"]
password = data["password"]

client = MongoClient(f"mongodb://{username}:" +
                     urllib.parse.quote(password) + "@127.0.0.1/feeds")


DB = client["feeds"]
users = DB["users"]
feeds = DB["feeds"]
