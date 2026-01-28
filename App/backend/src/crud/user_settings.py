from sqlalchemy.orm import Session
from .base import CRUDBase
from db.models.user import UserSettings

class CRUDUserSettings(CRUDBase[UserSettings]):
    def get_for_user(self, db: Session, user_id: str):
        return db.get(UserSettings, user_id)

user_settings_crud = CRUDUserSettings(UserSettings)
