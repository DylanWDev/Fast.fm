from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(TIMESTAMP)

    to_playlist = relationship("PlaylistListener", back_populates="to_user")
