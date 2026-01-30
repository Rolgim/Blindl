from datetime import date

from geoalchemy2 import Geography
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import Float

from ..base import Base


class Profile(Base):
    __tablename__ = "profiles"
    user_id = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="CASCADE"), 
        primary_key=True,
        nullable=False
        )
    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str | None] = mapped_column(String(500))
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    location: Mapped[str | None] = mapped_column(Geography(geometry_type='POINT', srid=4326))
    user = relationship("User", backref="profile", uselist=False)
    preferences = relationship(
        "ProfilePreferences",
        back_populates="profile",
        uselist=False,
        cascade="all, delete-orphan",
    )


class ProfilePreferences(Base):
    __tablename__ = "profile_preferences"

    profile_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("profiles.user_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    min_age: Mapped[int] = mapped_column(Integer, default=18, nullable=False)
    max_age: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    distance_km: Mapped[int] = mapped_column(Integer, default=50, nullable=False)

    profile = relationship("Profile", back_populates="preferences")
