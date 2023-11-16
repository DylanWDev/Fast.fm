from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    to_artist = relationship("AlbumArtist", back_populates="to_album")
