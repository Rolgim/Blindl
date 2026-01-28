from sqlalchemy.orm import Session

from db.models.profile import Profile

from .base import CRUDBase


class CRUDProfile(CRUDBase[Profile]):
    def get_for_user(self, db: Session, user_id: str):
        return db.get(Profile, user_id)

profile_crud = CRUDProfile(Profile)
