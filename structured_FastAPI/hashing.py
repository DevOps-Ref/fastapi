from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordHash:
    def bcrypt(passwd):
        return pwd_context.hash(passwd)
    
    def verify(plain_passwd:str , hashed_passwd:str):
        return pwd_context.verify(plain_passwd,hashed_passwd)