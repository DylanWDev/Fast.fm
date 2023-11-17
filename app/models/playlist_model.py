from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from database import Base
from app.models.user_model import User
from app.models.song_model import SongPlaylist


class PlaylistListener(Base):
    __tablename__ = "playlist_listener"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    playlist_id: Mapped[int] = mapped_column(Integer, ForeignKey("playlist.id"))
    user_id: Mapped[int] = Column(Integer, ForeignKey("user.id"))

    playlist: Mapped[List["Playlist"]] = relationship(back_populates="listeners")
    user: Mapped[List["User"]] = relationship(back_populates="playlist_listeners")

class Playlist(Base):
    __tablename__ = "playlist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, index=True)
    creater_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

    creator: Mapped[List["User"]] = relationship(back_populates="playlists")
    songs: Mapped[List["SongPlaylist"]] = relationship(back_populates="playlists")
    listeners: Mapped[List["PlaylistListener"]] = relationship(back_populates="playlist_listeners")
