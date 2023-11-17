from fastapi import FastAPI
# from app.models import User, Song, SongArtist, Artist, Playlist, PlaylistListener, Album, AlbumArtist
from database import engine, Base

from app.api.album_routes import router

app = FastAPI()
app.include_router(router)

def create_tables():
	Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
