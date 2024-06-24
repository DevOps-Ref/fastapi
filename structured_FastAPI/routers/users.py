from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from ..hashing import PasswordHash
from ..database import Base, get_db
from ..schemas import user, relation
from .. import models
from typing import List


router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get('/',
            response_model=List[relation.ShowUser])# List[user.UserResponse]
def fetch_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()



@router.get('/{id}',
            response_model=user.UserResponse)
def fetch_userBy_ID(id:int,
                    db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == id ).first()


@router.post('/create',
             response_model=user.UserResponse,
             status_code=status.HTTP_201_CREATED)
def create_user(request:user.UserCreate,
                db: Session = Depends(get_db),):
    data = request.dict()
    data['password'] =  PasswordHash.bcrypt(data['password'])
    user_data = models.User(**data)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return data