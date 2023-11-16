from fastapi import FastAPI
import app.models
import app.api
from database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
