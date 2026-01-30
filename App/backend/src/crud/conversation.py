
from uuid import UUID

from sqlalchemy.orm import Session

from db.models.conversation import Conversation

from .base import CRUDBase


class CRUDConversation(CRUDBase[Conversation]):
    def get_for_user(self, db: Session, user_id: UUID):
        return db.get(Conversation, user_id)
    
    def get_by_match_id(self, db: Session, match_id: UUID):
        return db.query(Conversation).filter(Conversation.match_id == match_id).first()

conversation_crud = CRUDConversation(Conversation)