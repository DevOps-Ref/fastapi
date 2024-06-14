from fastapi import FastAPI, Depends
from BLOG import req_body
from typing import Generator
from sqlalchemy.orm import Session
from BLOG.database import SessionLocal
from BLOG.models import User

app = FastAPI()

def get_db() -> Generator[Session,None,None] :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/register', status_code=201)
def create_user(request_body: req_body.user, db: Session = Depends(get_db) ):
    req_dict = request_body.dict()
    user_data = User(**req_dict)
    db.add(user_data)
    db.commit()
    # db.refresh(instance) is used to reload the attributes of a given instance from the database. 
    # This is particularly useful if you need to ensure that the instance has the most up-to-date values after some changes have been committed to the database.
    db.refresh(user_data)
    return user_data
