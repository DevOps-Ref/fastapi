from pydantic import BaseModel
from typing import List


class BlogRelation(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class UserRelation(BaseModel):
    name: str
    email : str
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: UserRelation
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    name: str
    #password: str
    email : str
    blogs : List[BlogRelation]

    class Config:
        orm_mode = True