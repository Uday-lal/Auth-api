import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.users import Users
from models.feeds import Feeds
from base import *
import redis
import secrets


app = FastAPI()
redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)


def get_token():
    while True:
        token = secrets.token_hex(28)
        if token not in redis_client.scan_iter("*"):
            return token


@app.get("/")
def get_users():
    users = Users()
    return users.read_all()


@app.get("/user/{user_id}")
def get_user(user_id: str):
    users = Users()
    user_data = users.read(user_id)
    user_data["_id"] = str(user_data["_id"])
    return user_data


@app.post("/register")
def register(user: UsersModel):
    document = {
        "user_name": user.user_name,
        "email": user.email,
        "password": user.password,
    }
    users = Users()
    users.create(document)
    return JSONResponse(status_code=201, content={"message": "User created"})


@app.post("/login")
def login(user: UsersModel):
    users = Users()
    user_data = users.query({"email": user.email})
    if user_data:
        user_id = str(user_data["_id"])
        if user_data["password"] == user.password:
            sid = get_token()
            user_data["_id"] = user_id
            user_data["sid"] = sid
            redis_client.set(sid, user_id)
            return user_data
        else:
            return JSONResponse(status_code=401, content={"message": "Invalid password"})
    else:
        return JSONResponse(status_code=401, content={"message": "Invalid email"})


@app.post("/feed")
def create_feed(feed: FeedModel):
    try:
        user_id = redis_client.get(feed.sid).decode("utf-8")
        feed_document = {
            "user_id": user_id,
            "feed": feed.feed
        }
        feeds = Feeds()
        feeds.create(feed_document)
        return JSONResponse(status_code=201, content={"message": "Feed created"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Something went wrong :("})


@app.get("/authenticate-token")
def authenticate_token(user: UsersModel):
    sid = user.sid
    if sid in redis_client.scan_iter("*"):
        return JSONResponse(status_code=200, content={"is_autherised": True})
    else:
        return JSONResponse(status_code=401, content={"is_autherised": False})


@app.delete("/delete/{user_id}")
def delete(user_id: str):
    try:
        users = Users()
        users.delete(user_id)
        return JSONResponse(status_code=200, content={"message": "User deleted"})
    except Exception:
        return JSONResponse(status_code=500, content={"message": "Something went wrong :("})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
