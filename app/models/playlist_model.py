from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    creater_id = Column(Integer, ForeignKey("user.id"))

    to_song = relationship("SongPlaylist", back_populates="to_playlist")
    to_user2 = relationship("PlaylistListener", back_populates="to_playlist2")
