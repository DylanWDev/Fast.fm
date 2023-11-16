from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class PlaylistListener(CustomBase):
    __tablename__ = "playlist_listener"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    playlist = relationship("Playlist", back_populates="listeners")
    user = relationship("User", back_populates="playlists")
