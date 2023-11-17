from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class SongArtist(Base):
    __tablename__ = "song_artist"
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))
    song = relationship("Song", back_populates="artists")
    artist = relationship("Artist", back_populates="songs")

class SongPlaylist(Base):
    __tablename__ = "song_playlist"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    
    song = relationship("Song", back_populates="playlists")
    playlist = relationship("Playlist", back_populates="songs")

class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    album_id = Column(Integer, ForeignKey("album.id"))

    album = relationship("Album", back_populates="songs")
    artists = relationship("Artist", secondary=SongArtist, back_populates="songs")
    playlists = relationship("Playlist", secondary=SongPlaylist, back_populates="songs")
