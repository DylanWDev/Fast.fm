from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class AlbumArtist(Base):
    __tablename__ = "album_artist"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("album.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    to_album = relationship("Album", back_populates="to_artist")
    to_artist = relationship("Artist", back_populates="to_album2")
