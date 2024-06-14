from pydantic import BaseModel

class user(BaseModel):
    userName: str
    type: str
    addr : str
    phone: int