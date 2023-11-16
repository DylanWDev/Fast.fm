from sqlalchemy import Column, String, Integer, Date, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base_model import Base
from app.models.album_model import AlbumArtist


class Artist(Base):
    __tablename__ = "album"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)

    to_album2: Mapped[List["AlbumArtist"]] = relationship(back_populates="to_artist")