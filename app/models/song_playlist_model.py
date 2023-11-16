from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import CustomBase

class SongPlaylist(CustomBase):
    __tablename__ = "song_playlist"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    playlist_id = Column(Integer, ForeignKey("playlist.id"))

    song = relationship("Song", back_populates="playlists")
    playlist = relationship("Playlist", back_populates="songs")
