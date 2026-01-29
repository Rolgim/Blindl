from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConversationCreate(BaseModel):
    match_id: UUID

class ConversationRead(BaseModel):
    id: UUID
    match_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)