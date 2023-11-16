from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.id"))

    to_playlist2 = relationship("SongPlaylist", back_populates="to_song2")
