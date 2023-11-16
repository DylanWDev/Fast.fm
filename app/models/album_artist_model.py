from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class AlbumArtist(CustomBase):
    __tablename__ = "album_artist"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("album.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    album = relationship("Album", back_populates="artists")
    artist = relationship("Artist", back_populates="albums")
