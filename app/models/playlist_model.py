from sqlalchemy import Column, String, Integer, Date, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base_model import Base


class Playlist(Base):
    __tablename__ = "playlist"

    id: Mapped[id] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    creater_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    to_song: Mapped[List["SongPlaylist"]] = relationship(back_populates="to_playlist")
    to_user2: Mapped[List["PlaylistListener"]] = relationship(back_populates="to_playlist2")


class SongPlaylist(Base):
    __tablename__ = "song_playlist"
     
    id: Mapped[id] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("song.id"))
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlist.id"))

    to_playlist: Mapped[List["Playlist"]] = relationship(back_populates="to_song")
    to_song2: Mapped[List["Song"]] = relationship(back_populates="to_playlist2")