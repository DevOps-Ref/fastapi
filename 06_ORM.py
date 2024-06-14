from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.dialects.mysql import VARCHAR, CHAR

from urllib.parse import quote
import uvicorn
from pydantic import BaseModel



db_user = "root"
db_password = "banner@456"

# we encode because @ in password is causing error
encoded_password = quote(db_password)

DATABASE_URL = f"mysql+pymysql://{db_user}:{encoded_password}@localhost:3306/mydb"

#1. Lets create engine which forms connection to our database
# connect_args={"check_same_thread": False} argument is needed only for sqlite
engine = create_engine(DATABASE_URL)

# 2. session manages conversation b/w python application and database
# It return a class which is used to create multiple sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. declarative_base() function return class,  // deprecated :: use DeclarativeBase class
# Base = declarative_base()
class Base(DeclarativeBase):
    pass

# Base.metadata.create_all(bind=engine) # used to create all the tables that are defined in your SQLAlchemy models
# 4. create models / classes which subclasses | Inherits from Base class
class Blog(Base):
    '''
        This is a model
            * Apply limit on Interger values
        General Args
            * nullable = False --> NOT NULL 

            name=,autoincrement=,default=,key=,doc=index=,unique=,nullable= False,onupdate=,primary_key=,
    '''
    __tablename__ ="blogtable"
    id = Column(Integer,primary_key=True)
    title = Column(String(15))
    body = Column(VARCHAR(25))

# Base.metadata.create_all(engine) # create all the tables

# Create Requestbody
class Blog_request(BaseModel):
    id : int
    title: str
    body : str
app = FastAPI()

# Return session
from typing import Generator
def get_db() -> Generator[Session,None,None] :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@app.post('/createblog')
def create_blog(request:Blog_request, db: Session =  Depends(get_db)):
    new_blog = Blog(id=request.id,title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

