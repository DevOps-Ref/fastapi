# FASTAPI
## SETUP
        pip install fastapi
            fastapi
            starlette
            pydantic
        pip install uvicorn

## START SERVER
* RUN from COMMAND PROMPT
```
    uvicorn <python file>:<Fastapi object> --reload 
            reload :: to reload the sever every time it is saved 
```
* RUN in Python code
```
    uvicorn.run("<python file>:<FastAPI object>",host="localhost",reload=True)
```

# BASIC API (01_Basic.py)
```
    from fastapi import FastAPI
    import uvicorn
    app = FastAPI()

    @app.get('/') # /  :: path / endpoint / route
    def BasicAPI():
        return "Basic_API"

    if __name__ == "__main__":
        uvicorn.run("01_Basic:app",host="localhost",reload=True)
```


# Terminology
* <mark> PATH </mark>  ::  /about
* <mark>OPERATION </mark>  :: get | post
* <mark>PATH OPERATION FUNCTION </mark>:: function

# PATH PARAMETER (02_Path_Parameters.py)
* By specifying path parameter datatype
        * We can perform typecasting(Done by pydantic under the hood)
        * We can perform datatype validation
* If datatype is not specified then it accepts any value.
```
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def home():
        return "Please Enter id in path as Path parameter"

    @app.get("/{id}")
    def get_id_desc(id: int):
        return {id: "the id given as path parameter"}
```

## IMPACT OF ORDER OF "PATH OPEARTION FUNCTIONS" (03_Order_Impact.py)
* The Path matching is done from top to bottom and it stops looking after the first match is found.
* So order is important

E.G : TRY  finding <mark><b> /about </b></mark> path in Both scenarios



<div style="display:flex;">

<div>
<pre style="display:inline-block;background-color:green;">
@app.get("/about")
def get_id_desc():
    return {"data" : "this is about page"}

@app.get("/{id}")
def get_id_desc(id: int):
    return {"data" : id}
</pre>
</div>

<div>
<pre style="display:inline-block;background-color:red;">
@app.get("/{id}")
def get_id_desc(id: int):
    return {"data" : id}

@app.get("/about")
def get_id_desc():
    return {"data" : "this is about page"}
</pre>
</div>

</div>


# QUERY PARAMETER
<b>NOTE</b>:
* <mark><b> Specify default values </b></mark> for Query parameters or-else <u>error is thrown when we miss providing values</u> to "limit, published"
* Specify Optional Values
* We can pass any number of parameters

```
@app.get("/blog")
def get_blogs(limit:int = 10,published:bool = True, sort:Optional['str']=None):
    if published:
        return f"Here are the {limit} blogs from the published blogs"
    else:
        return f"Here are the {limit} blogs from all the blogs"
```

# REQUEST BODY (05_Request_Body.py)
* <b>REQUEST BODY</b> is <mark><b> Data sent by client  </b></mark>
* PYDANTIC MODELS are used to declare request body

```
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# Declaring Request BODY
# This provides an example in docs
class Post_Data(BaseModel):
    id: int
    name: str
    salary: float
    caste: Optional['str']

app = FastAPI()

# Specify tags if you want
@app.get("/emp_details", tags=["EMP_DETAILS"])
def home():
    return "hello"

@app.post("/emp_details/create", tags=["EMP_DETAILS"])
def create_emp(emp_details:Post_Data):
    print(emp_details,list(emp_details))
    return (emp_details)
```

# ORM (OBJECT RELATION MAPPING)
* ORM library has tools to convert b/w <mark>OBJECTS</mark> in code to database <mark> TABLES </mark>
* this Conversion is called Mapping.
* ORMs also have tools to make the connections or relations between tables or entities.
* Say you have class PET , OWNER. NOw PET has attributes type, owner. Instance of PET orion_cat has [type=cat,owner=jhon].Instance of OWNER jhon has [name=jhon,mobile=567]. orion_cat.owner.mobile will fetch owners mobile from OWNER TABLE

* FastAPI works with any ORM library
    * SQLAlchemy :: You can use this to connect to anytype of database (INDEPENDANT of FRAMEWORK)
        * PostgreSQL
        * MySQL
        * SQlite
        * Oracle
    * DJANGO -ORM :: limited to DJANGO

## GENERAL PROCESS
### 1. DATABASE.py
1. Create ENGINE :: which form connection to database
2. Create session :: which manages conversation b/w python application and database
3. Create Base class
```
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

db_user = "root"
db_password = "banner@423"

# we encode because @ in password is causing error
encoded_password = quote(db_password)

DATABASE_URL = f"mysql+pymysql://{db_user}:{encoded_password}@localhost:3306/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
```
### 2. MODELS.py
* create a class that represents a table in a SQL database, each attribute of the class represents a column, with a name and a type.
* Execute <mark><b> Base.metadata.create_all(engine) </b></mark> to create tables
```
from BLOG.database import Base, engine
from sqlalchemy.dialects.mysql import VARCHAR, CHAR
from sqlalchemy import Enum, Column, Integer
import enum

class usertype(enum.Enum):
    Patient = "Patient"
    Practitioner = "Practitioner"
    Doctor = "Doctor"
    Hospital = "Hospital"

class User(Base):
    __table__ = "user"
    userId = Column(Integer,index=True)
    userName = Column(VARCHAR(20))
    type = Column(Enum(usertype),nullable=False)
    addr = Column(VARCHAR(20))
    phone = Column(Integer)

Base.metadata.create_all(engine)
```

### 3. req_body.py
```
from pydantic import BaseModel

class user(BaseModel):
    userName: str
    type: str
    addr : str
    phone: int
```

### main.py
```
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

```

* uvicorn BLOG.main:app --reload


