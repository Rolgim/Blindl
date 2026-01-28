from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.user import User

from .base import CRUDBase


class CRUDUser(CRUDBase[User]):
    def get_by_email(self, db: Session, email: str):
        stmt = select(User).where(User.email == email)
        return db.scalar(stmt)

    def get_by_username(self, db: Session, username: str):
        stmt = select(User).where(User.username == username)
        return db.scalar(stmt)

user_crud = CRUDUser(User)
