from fastapi import FastAPI
from app.models import User, Song, SongArtist, Artist, Playlist, PlaylistListener, Album, AlbumArtist
from database import engine, Base


app = FastAPI()

def create_tables():
	Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
