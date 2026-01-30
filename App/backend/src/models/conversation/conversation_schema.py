from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConversationCreate(BaseModel):
    """
    Schema for creating a new conversation.
    match_id: UUID of the match the conversation belongs to.
    """
    match_id: UUID

class ConversationRead(BaseModel):
    """
    Schema for reading conversation information.
    id: UUID of the conversation.
    match_id: UUID of the match the conversation belongs to.
    created_at: datetime when the conversation was created.
    """
    id: UUID
    match_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)