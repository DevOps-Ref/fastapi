from pydantic import BaseModel
from typing import Optional, List

class UserCreate(BaseModel):
    name: str
    email : str
    password: str


class UserUpdate(BaseModel):
    name: Optional['str']
    email : Optional['str']
    password:Optional['str']

class UserResponse(BaseModel):
    id: int
    name: str
    #password: str
    email : str

    class Config:
        orm_mode = True

