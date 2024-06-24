from fastapi import FastAPI, Depends, status, Response, HTTPException
from BLOG import req_body
from typing import Generator, List
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

@app.post('/register', status_code=status.HTTP_201_CREATED) # status_code=201 
def create_user(request_body: req_body.user, db: Session = Depends(get_db) ):
    req_dict = request_body.dict()
    user_data = User(**req_dict)
    db.add(user_data)
    db.commit()
    # db.refresh(instance) is used to reload the attributes of a given instance from the database. 
    # This is particularly useful if you need to ensure that the instance has the most up-to-date values after some changes have been committed to the database.
    db.refresh(user_data)
    return user_data

@app.get("/fetch", response_model=List[req_body.Response_model])
def fetch_all(db: Session = Depends(get_db)):
    return db.query(User).all()
    #return db.query(User).limit(1).all()

@app.get("/fetch/{id}", response_model=List[req_body.response_model])
def fetch_by_id(response: Response, db : Session= Depends(get_db),id:int=1 ):
    data = db.query(User).filter(User.userId == id).all()
    if not data:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"data for id :{id} is not available"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data for id :{id} is not available")
    else:
        return data
    
@app.delete("delete/{id}")
def delete(id: int,db: Session = Depends(get_db)):
    db.query(User).filter(User.userId == id).delete(synchronize_session=False)
    db.commit()
    return "done"

# Have seperate schema for updating
@app.put('/update_req/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_requied(id: int, request_body:req_body.user_update, db: Session = Depends(get_db)):
    data_list = db.query(User).filter(User.userId == id)
    if not data_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The data is not available to update")
    else:
        # exclude_unset removes all the keys whose value is None
        data_list.update(request_body.dict(exclude_unset=True),synchronize_session=False)    
        db.commit()
        return "updated"

@app.post('/test')
def test(request:req_body.test ):
    return request