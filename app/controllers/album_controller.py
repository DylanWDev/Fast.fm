from sqlalchemy.orm import Session, joinedload
from app.models.album_model import Album
from app.schemas.album_schema import AlbumSchema
from app.models.artist_model import AlbumArtist
from app.models.song_model import Song

def list_album(db: Session, skip: int = 0, limit: int = 100):
    return(
    db.query(Album)
    .offset(skip)
    .limit(limit)
    .all()
    )