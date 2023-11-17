from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from database import Base


class Album(Base):
    __tablename__ = "album"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, index=True)

    artists: Mapped[List["AlbumArtist"]] = relationship(back_populates="album")
    songs: Mapped[List["Song"]] = relationship(back_populates="album")
