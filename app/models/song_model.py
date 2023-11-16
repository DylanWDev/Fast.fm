from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class Song(CustomBase):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.id"))

    artists = relationship("SongArtist", back_populates="song")
    playlists = relationship("SongPlaylist", back_populates="song")
