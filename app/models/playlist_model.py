from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.models.base_model import Base


class PlaylistListener(Base):
    __tablename__ = "playlist_listener"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlist.id"))
    user_id: Mapped[int] = Column(ForeignKey("user.id"))

    playlist: Mapped[List["Playlist"]] = relationship(back_populates="listeners")
    user: Mapped[List["User"]] = relationship(back_populates="playlist_listeners")

class Playlist(Base):
    __tablename__ = "playlist"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(index=True)
    creater_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    creator: Mapped[List["User"]] = relationship(back_populates="playlists")
    songs: Mapped[List["SongPlaylist"]] = relationship(back_populates="playlist")
    listeners: Mapped[List["PlaylistListener"]] = relationship(back_populates="playlist")
