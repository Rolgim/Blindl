from geoalchemy2 import WKTElement
from sqlalchemy.orm import Session

from db.models.profile import Profile

from .base import CRUDBase


class CRUDProfile(CRUDBase[Profile]):
    def get_for_user(self, db: Session, user_id: str):
        return db.get(Profile, user_id)
    
    def update(self, db: Session, db_obj: Profile, obj_in: dict):
        if "location" in obj_in and obj_in["location"]:
            obj_in["location"] = WKTElement(obj_in["location"], srid=4326)
        return super().update(db, db_obj, obj_in)


profile_crud = CRUDProfile(Profile)
