from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str | None] = mapped_column(String(500))

    user = relationship("User", backref="profile", uselist=False)
    preferences = relationship(
        "ProfilePreferences",
        back_populates="profile",
        uselist=False,
        cascade="all, delete-orphan",
    )


class ProfilePreferences(Base):
    __tablename__ = "profile_preferences"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    profile_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("profiles.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    min_age: Mapped[int | None]
    max_age: Mapped[int | None]
    distance_km: Mapped[int | None]

    profile = relationship("Profile", back_populates="preferences")
