
from sqlalchemy.orm import Session

from db.models.conversation import Conversation

from .base import CRUDBase


class CRUDConversation(CRUDBase[Conversation]):
    def get_for_user(self, db: Session, match_id: str):
        return db.get(Conversation, match_id)
        