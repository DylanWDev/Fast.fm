from typing import Optional
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP

class UserSchema(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    created_at: Optional[TIMESTAMP] = None