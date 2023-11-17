from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class PlaylistListener(Base):
    __tablename__ = "playlist_listener"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    playlist = relationship("Playlist", back_populates="listeners")
    user = relationship("User", back_populates="playlist_listeners")

class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    creater_id = Column(Integer, ForeignKey("user.id"))

    creator = relationship("User", back_populates="playlists")
    songs = relationship("SongPlaylist", back_populates="playlists")
    listeners = relationship("PlaylistListener", back_populates="playlist_listeners")
