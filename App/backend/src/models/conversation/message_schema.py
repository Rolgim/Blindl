from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, constr


# From client to API
class MessageCreate(BaseModel):
    conversation_id: UUID
    content: str

# From API to client
class MessageRead(BaseModel):
    id: UUID
    conversation_id: UUID
    sender_id: UUID
    content: constr(max_length=2000)
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)