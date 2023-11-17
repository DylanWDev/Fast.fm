from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from app.schemas.album_schema import AlbumSchema
import app.utils

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routes.post('/create_album')
async def create_album(request: AlbumSchema, db:Session = Depends(get_db)):
    return app.utils.create_album(db, request)