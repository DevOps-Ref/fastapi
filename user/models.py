from user.database import Base, engine
from sqlalchemy.dialects.mysql import VARCHAR, CHAR
from sqlalchemy import Column, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from typing import Optional

class User(Base):
    __tablename__ = "latest_user"

    userId = Column(Integer,index=True,primary_key=True)
    userName = Column(VARCHAR(20))
    type = Column(VARCHAR(10),nullable=False)
    addr = Column(VARCHAR(20))
    phone = Column(Integer)
    yob = Column(Integer)
    # age = column_property(2024-yob)
    

    @hybrid_property
    def age(self):
        return 2024-self.yob
    
User.my_age = column_property(2024-User.yob)

# HYBRID VS COLUMN PROPERTY :: Both can be used in queries, but in hybrid python logic can be implemented.
Base.metadata.create_all(engine)