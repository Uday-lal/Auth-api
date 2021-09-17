from . import users
from bson.objectid import ObjectId


class Users:
    def __init__(self):
        self.users = users

    def create(self, data: dict):
        print(data)
        self.users.insert_one(data)

    def update(self, user_id, updated_data: dict):
        self.users.update_one({"_id": user_id}, {"$set": updated_data})

    def read(self, user_id):
        return self.users.find_one({"_id": ObjectId(user_id)})

    def query(self, query_data: dict):
        return self.users.find_one(query_data)

    def read_all(self):
        users_data = []
        results = self.users.find({})
        for result in results:
            result["_id"] = str(result["_id"])
            users_data.append(result)
        return users_data

    def delete(self, user_id):
        self.users.delete_one({"_id": ObjectId(user_id)})
