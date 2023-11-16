from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class Album(CustomBase):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    artists = relationship("AlbumArtist", back_populates="album")
    songs = relationship("Song", back_populates="album")
