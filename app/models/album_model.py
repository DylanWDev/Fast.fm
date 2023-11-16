from sqlalchemy import Column, String, Integer, Date, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base_model import Base



class Album(Base):
    __tablename__ = "album"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String)

    to_artist: Mapped[List["AlbumArtist"]] = relationship(back_populates="to_album")




class AlbumArtist(Base):
    __tablename__ = "album_artist"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"))

    to_album: Mapped[List["Album"]] = relationship(back_populates="to_artist")
    to_artist: Mapped[List["Artist"]] = relationship(back_populates="to_album2")