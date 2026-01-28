import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    conversation_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("conversations.id", ondelete="CASCADE"),
        nullable=False,
    )

    sender_id: Mapped[str] = mapped_column(
        CHAR(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    conversation = relationship("Conversation", back_populates="messages")
    sender = relationship("User")
