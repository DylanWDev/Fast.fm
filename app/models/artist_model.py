from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from database import Base

class AlbumArtist(Base):
    __tablename__ = "album_artist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    album_id: Mapped[int] = mapped_column(Integer, ForeignKey("album.id"))
    artist_id: Mapped[int] = mapped_column(Integer, ForeignKey("artist.id"))

    album: Mapped[List["Album"]] = relationship(back_populates="artists")
    artist: Mapped[List["Artist"]] = relationship(back_populates="albums")

class SongArtist(Base):
    __tablename__ = "song_artist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(Integer, ForeignKey("song.id"))
    artist_id: Mapped[int] = mapped_column(Integer, ForeignKey("artist.id"))

    song: Mapped[List["Song"]] = relationship(back_populates="artists")
    artist: Mapped[List["Artist"]] = relationship(back_populates="songs")

class Artist(Base):
    __tablename__ = "artist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, index=True)

    albums: Mapped[List["AlbumArtist"]] = relationship(back_populates="artists")
    songs: Mapped[List["SongArtist"]] = relationship(back_populates="artists")
