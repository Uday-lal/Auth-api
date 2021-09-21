from pydantic import BaseModel
from typing import Optional


class UsersModel(BaseModel):
    sid: Optional[str]
    user_name: Optional[str]
    email: str
    password: str


class FeedModel(BaseModel):
    sid: str
    feed: str
