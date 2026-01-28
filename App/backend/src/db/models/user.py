import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    settings = relationship(
        "UserSettings",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

class UserSettings(Base):
    __tablename__ = "user_settings"

    user_id = mapped_column(
        CHAR(36), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    language = mapped_column(String(5), default="en")
    email_notifications = mapped_column(Boolean, default=True)
    weekly_pool_enabled = mapped_column(Boolean, default=True)

    user = relationship("User", back_populates="settings")