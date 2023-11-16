from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class Artist(CustomBase):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    songs = relationship("SongArtist", back_populates="artist")
    albums = relationship("AlbumArtist", back_populates="artist")
