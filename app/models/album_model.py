from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class AlbumArtist(Base):
    __tablename__ = "album_artist"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("album.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    album = relationship("Album", back_populates="artists")
    artist = relationship("Artist", back_populates="albums")

class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    artists = relationship("Artist", secondary=AlbumArtist, back_populates="albums")
    songs = relationship("Song", back_populates="album")
