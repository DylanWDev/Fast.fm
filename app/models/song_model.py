from sqlalchemy import Column, String, Integer, Date, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base_model import Base
from app.models.playlist_model import SongPlaylist



class Song(Base):
    id: Mapped[id] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"))

    to_playlist2: Mapped[List["SongPlaylist"]] = relationship(back_populates="to_song2")