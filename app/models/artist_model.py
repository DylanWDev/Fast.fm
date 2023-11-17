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

class SongArtist(Base):
    __tablename__ = "song_artist"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    song = relationship("Song", back_populates="artists")
    artist = relationship("Artist", back_populates="songs")

class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    albums = relationship("AlbumArtist", back_populates="artists")
    songs = relationship("SongArtist", back_populates="artists")
