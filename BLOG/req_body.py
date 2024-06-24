from pydantic import BaseModel
from typing import Optional, Literal 

class user(BaseModel):
    userName: str
    type: str
    addr : str
    phone: int

class user_update(BaseModel):
    userName: Optional[str] = None
    type: Optional[str] = None
    addr : Optional[str] = None
    phone: Optional[int] = None

class test(BaseModel):
    type: Literal["Hospital","Doctor","Practitioner","Student"]

class response_model(BaseModel):
    userName : str  # attributes same as user
    phone : int
    class Config:
        orm_mode = True

class Response_model(user):
    class Config:
        orm_mode = True
