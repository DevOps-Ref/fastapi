from sqlalchemy import Column, Integer, ForeignKey
from .database import Base , engine
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import VARCHAR, CHAR


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(30))
    body = Column(VARCHAR(30))
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(30))
    email = Column(VARCHAR(30))
    password = Column(VARCHAR(100))

    blogs = relationship('Blog', back_populates="creator")

Base.metadata.create_all(engine)