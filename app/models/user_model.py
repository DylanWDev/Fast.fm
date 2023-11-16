from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class User(CustomBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(TIMESTAMP)

    playlists = relationship("PlaylistListener", back_populates="user")
