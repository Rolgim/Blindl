
from sqlalchemy.orm import Session

from db.models.message import Message

from .base import CRUDBase


class CRUDMessage(CRUDBase[Message]):
    def get_for_conversation(self, db: Session, conversation_id: str):
        return db.get(Message, conversation_id)