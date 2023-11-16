from fastapi import FastAPI
from app.models import User, Song, SongArtist, Artist, Playlist, PlaylistListener, Album, AlbumArtist
from database import engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
