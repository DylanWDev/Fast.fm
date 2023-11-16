from sqlalchemy import Column, String, Integer, Date, ForeignKey, TIMESTAMP
from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base_model import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    password:  Mapped[str] = Column(String)
    created_at:  Mapped[TIMESTAMP] = Column(TIMESTAMP)

    to_playlist: Mapped[List["PlaylistListener"]] = relationship(back_populates="to_user")


class PlaylistListener(Base):
    __tablename__ = "playlist_listener"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlist.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    to_user: Mapped[List["PlaylistListener"]] = relationship(back_populates="to_playlist")
    to_playlist2: Mapped[List["Playlist"]] = relationship(back_populates="to_user2")
    