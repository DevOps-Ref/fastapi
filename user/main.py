from fastapi import FastAPI, status, Depends
from user import schemas, database, models
from typing import Generator, List
from sqlalchemy import select
from sqlalchemy.orm  import Session

app = FastAPI()

def get_db() -> Generator[Session,None,None] :
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get(
    "/user",
    tags=['user'],
    response_model =List[schemas.UserResponse],
    status_code= status.HTTP_200_OK
)
def fetch_all(db: Session = Depends(get_db)):
    return db.query(models.User).all()



@app.post(
    '/create',
    tags=['user'],
    status_code=status.HTTP_201_CREATED
)
def create(request: schemas.UserCreateRequest, db: Session = Depends(get_db)):
    user_data = models.User(**request.dict())
    db.add(user_data)
    # db.add_all([item1, item2, item3])
    db.commit()
    db.refresh(user_data)
    return "created"


@app.get('/user/select')
def fetch(db: Session = Depends(get_db)):
    return db.scalars(select(models.User).where(models.User.age > 100)).all()