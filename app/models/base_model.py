from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from app.models.album_model import Album, AlbumArtist
from app.models.artist_model import Artist
from app.models.playlist_model import Playlist, SongPlaylist
from app.models.song_model import Song
from app.models.user_model import User, PlaylistListener