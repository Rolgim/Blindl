
from uuid import UUID

from sqlalchemy.orm import Session

from db.models.message import Message

from .base import CRUDBase


class CRUDMessage(CRUDBase[Message]):
    def get_for_conversation(self, db: Session, conversation_id: UUID):
        return (
            db.query(self.model)
            .filter(
                    self.model.conversation_id == conversation_id,
            )
            .order_by(self.model.created_at.desc())
            .all()
        )
    
message_crud = CRUDMessage(Message)