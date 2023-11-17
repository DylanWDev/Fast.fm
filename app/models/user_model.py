from sqlalchemy import Column, Integer, String, ForeignKey, Table, TIMESTAMP
from typing import List
from sqlalchemy.orm import relationship, Mapped, relationships, mapped_column
from app.models.base_model import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = Column(index=True)
    email: Mapped[str] = Column(index=True)
    password: Mapped[str] = Column(index=True)
    created_at: Mapped[str] = Column(index=True)

    playlists: Mapped[List["Playlist"]] = relationship(back_populates="creator")
    playlist_listeners: Mapped[List["PlaylistListener"]] = relationship(back_populates="user")
