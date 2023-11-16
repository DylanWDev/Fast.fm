from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base

class SongPlaylist(Base):
    __tablename__ = "song_playlist"
     
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    playlist_id = Column(Integer, ForeignKey("playlist.id"))

    to_playlist = relationship("Playlist", back_populates="to_song")
    to_song2 = relationship("Song", back_populates="to_playlist2")
