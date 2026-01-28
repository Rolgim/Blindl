from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    match_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("matches.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    match = relationship("Match", backref="conversation")
    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
    )
