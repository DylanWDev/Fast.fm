from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class Playlist(CustomBase):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    creater_id = Column(Integer, ForeignKey("user.id"))

    songs = relationship("SongPlaylist", back_populates="playlist")
    listeners = relationship("PlaylistListener", back_populates="playlist")