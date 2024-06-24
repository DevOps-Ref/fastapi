from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

db_user = "root"
db_password = "banner@456"

# we encode because @ in password is causing error
encoded_password = quote(db_password)

DATABASE_URL = f"mysql+pymysql://{db_user}:{encoded_password}@localhost:3306/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()