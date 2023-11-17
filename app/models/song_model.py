from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.models.base_model import Base


class SongPlaylist(Base):
    __tablename__ = "song_playlist"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("song.id"))
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlist.id"))

    #song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))

    song: Mapped[List["Song"]] = relationship(back_populates="playlists")
    playlist: Mapped[List["Playlist"]] = relationship(back_populates="songs")

class Song(Base):
    __tablename__ = "song"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, index=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"))

    album: Mapped[List["Album"]] = relationship(back_populates="songs")
    artists: Mapped[List["SongArtist"]] = relationship(back_populates="song")
    playlists: Mapped[List["SongPlaylist"]] = relationship(back_populates="song")

    #artist = relationship("Artist", back_populates="songs")
