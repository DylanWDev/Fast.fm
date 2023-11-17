from sqlalchemy.orm import DeclarativeBase
from app.models.album_model import Album
from app.models.artist_model import Artist, SongArtist, AlbumArtist
from app.models.playlist_model import Playlist, PlaylistListener
from app.models.song_model import Song, SongArtist, SongPlaylist
from app.models.user_model import User

class Base(DeclarativeBase):
    pass