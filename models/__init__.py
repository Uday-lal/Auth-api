from pymongo import MongoClient
import urllib.parse
import json

file = open("config.json", "r")
data = json.load(file)
username = data["username"]
password = data["password"]

client = MongoClient(f"mongodb://{username}:" +
                     urllib.parse.quote(password) + "@127.0.0.1/feeds")


DB = client["feeds"]
users = DB["users"]
feeds = DB["feeds"]
