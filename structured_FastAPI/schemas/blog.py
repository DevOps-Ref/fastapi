from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    body: str


class BlogResponse(BaseModel):
    title: str
    body: str
    user_id :int
    class Config:
        orm_mode = True



