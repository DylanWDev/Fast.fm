from sqlalchemy.orm import Session, joinedload
from app.models.album_model import Album
from app.schemas.album_schema import AlbumSchema

def create_game(db: Session, album: AlbumSchema):
    _album = Album(id=album.id, name=album.name)
    db.add(_album)
    db.commit()
    db.refresh(_album)
    return _album