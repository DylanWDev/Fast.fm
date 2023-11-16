from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class PlaylistListener(Base):
    __tablename__ = "playlist_listener"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    to_user = relationship("User", back_populates="to_playlist")
    to_playlist2 = relationship("Playlist", back_populates="to_user2")
