from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from app.schemas.album_schema import AlbumSchema
from app.controllers.album_controller import list_album

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/list_album/')
async def list_albums(db:Session = Depends(get_db)):
    return list_album(db)