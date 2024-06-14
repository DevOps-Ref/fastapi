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
    __tablename__ = "user"
    userId = Column(Integer,index=True,primary_key=True)
    userName = Column(VARCHAR(20))
    type = Column(Enum(usertype),nullable=False)
    addr = Column(VARCHAR(20))
    phone = Column(Integer)

Base.metadata.create_all(engine)