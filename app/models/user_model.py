from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    created_at = Column(String)

    playlists = relationship("Playlist", back_populates="creator")
    playlist_listeners = relationship("PlaylistListener", back_populates="listeners")
