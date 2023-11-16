from typing import Optional
from pydantic import BaseModel

class AlbumSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None