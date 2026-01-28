from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Profile(Base):
    __tablename__ = "profiles"

    user_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        )

    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str | None] = mapped_column(String(500))
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)

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
        nullable=False,
    )

    min_age: Mapped[int] = mapped_column(Integer, default=18, nullable=False)
    max_age: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    distance_km: Mapped[int] = mapped_column(Integer, default=50, nullable=False)

    profile = relationship("Profile", back_populates="preferences")
