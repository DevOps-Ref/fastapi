from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from ..hashing import PasswordHash
from ..database import Base, get_db
from ..schemas import blog ,relation
from .. import models
from typing import List
from .. import oAuth2

router = APIRouter(
    prefix='/blog',
    tags=['BLOG']
)

@router.post('/create',
             response_model=blog.BlogResponse)
def create_blog(request :blog.BlogCreate,
                user_id: int, 
                db: Session = Depends(get_db),
                current_user= Depends(oAuth2.get_current_user)):
    data = request.dict()
    data['user_id'] = user_id
    user_data = models.Blog(**data)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return data

@router.get('/',response_model= List[relation.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()
