from . import feeds


class Feeds:
    def __init__(self):
        self.feeds = feeds

    def create(self, data: dict):
        if "user_id" in data:
            self.feeds.insert_one(data)
        else:
            raise Exception("user_id in require to create a feed")

    def update(self, feed_id, updated_feed: str):
        self.feeds.update_one(
            {"_id": feed_id}, {"$set": {"feed": updated_feed}})

    def read(self, feed_id):
        self.feeds.find({"_id": feed_id})

    def read_all(self, user_id):
        return self.feeds.find({"user_id": user_id})

    def delete(self, feed_id):
        self.feeds.delete_one({"_id": feed_id})
