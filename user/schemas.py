from pydantic import BaseModel
from typing import Literal

#RESPONSE MODEL
class UserResponse(BaseModel):
    userName : str
    addr : str
    phone : int
    age: int

    class Config:
        orm_mode = True

# REQUEST BODY :: CREATE
class UserCreateRequest(BaseModel):
    userName : str
    type : Literal["Hospital","Doctor","Practitioner","Student"]
    addr: str
    phone : int
    yob : int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "userName": "Foo",
                    "type": "Hospital",
                    "addr": "AP",
                    "phone": 8978,
                    "yob":1998
                }
            ]
        }
    }