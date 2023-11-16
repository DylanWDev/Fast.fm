from sqlalchemy import Column, String, Integer, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(TIMESTAMP)