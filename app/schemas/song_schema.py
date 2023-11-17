from typing import Optional
from pydantic import BaseModel

class SongSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    album_id: Optional[int] = None

    class Config:
        orm_mode = True