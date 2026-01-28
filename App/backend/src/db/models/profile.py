from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Profile(Base):
    __tablename__ = "profiles"

    user_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        )

    display_name: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str | None] = mapped_column(String(500))
    birth_date: Mapped[date | None] = mapped_column(Date)

    user = relationship("User", backref="profile", uselist=False)
    preferences = relationship(
        "ProfilePreferences",
        back_populates="profile",
        uselist=False,
        cascade="all, delete-orphan",
    )


class ProfilePreferences(Base):
    __tablename__ = "profile_preferences"

    profile_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("profiles.user_id", ondelete="CASCADE"),
        primary_key=True,
    )

    min_age: Mapped[int | None]
    max_age: Mapped[int | None]
    distance_km: Mapped[int | None]

    profile = relationship("Profile", back_populates="preferences")
