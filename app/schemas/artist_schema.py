from typing import Optional
from pydantic import BaseModel

class ArtistSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None