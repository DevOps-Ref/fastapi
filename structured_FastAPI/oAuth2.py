from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
import jwt
from .schemas.authentication import TokenData
from . import token 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(my_token: Annotated[str, Depends(oauth2_scheme)]):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token.verify_token(my_token,credentials_exception)
