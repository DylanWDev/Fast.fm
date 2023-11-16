from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase


class SongArtist(CustomBase):
    __tablename__ = "song_artist"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    song = relationship("Song", back_populates="artists")
    artist = relationship("Artist", back_populates="songs")