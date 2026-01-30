from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, constr


# From client to API
class MessageCreate(BaseModel):
    """
    Schema for creating a new message in a conversation.
    conversation_id: UUID of the conversation the message belongs to.
    content: Content of the message.
    """
    conversation_id: UUID
    content: str

# From API to client
class MessageRead(BaseModel):
    """
    Schema for reading message information.
    id: UUID of the message.
    conversation_id: UUID of the conversation the message belongs to.
    sender_id: UUID of the user who sent the message.
    content: Content of the message.
    created_at: datetime when the message was created.
    """
    id: UUID
    conversation_id: UUID
    sender_id: UUID
    content: constr(max_length=2000)
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)