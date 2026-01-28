import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class MatchStatus(PyEnum):
    ACTIVE = "active"
    PAST = "past"


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[str] = mapped_column(
        CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False
        )
    user_a_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
        )
    user_b_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
        )
    status: Mapped[MatchStatus] = mapped_column(Enum(MatchStatus), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable = False)
    ended_at: Mapped[datetime | None] = mapped_column(nullable=True)

    user_a = relationship("User", foreign_keys=[user_a_id])
    user_b = relationship("User", foreign_keys=[user_b_id])
