from fastapi import FastAPI
import app.models
import app.api
from database import engine
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
