from fastapi import FastAPI,APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..schemas import authentication
from ..hashing import PasswordHash
from ..database import get_db
from ..models import User
from datetime import datetime, timedelta, timezone
from .. import token
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter(tags=['LOGIN'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm =Depends() ,
          db: Session = Depends(get_db) ):
    user = db.query(User).filter(User.email == request.username ).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    if not PasswordHash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return authentication.Token(access_token=access_token, token_type="bearer")