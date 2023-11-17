from sqlalchemy import Column, Integer, String, ForeignKey, Table
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.models.base_model import Base

class Album(Base):
    __tablename__ = "album"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(index=True)

    artists: Mapped[List["AlbumArtist"]] = relationship(back_populates="album")
    songs: Mapped[List["Song"]] = relationship(back_populates="album")
