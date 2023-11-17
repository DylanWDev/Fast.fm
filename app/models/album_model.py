from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    artists = relationship("AlbumArtist", back_populates="album")
    songs = relationship("Song", back_populates="album")
