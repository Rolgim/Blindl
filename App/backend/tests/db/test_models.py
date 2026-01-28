# tests/db/test_models.py
import pytest  # noqa: I001
from datetime import date

from sqlalchemy.exc import IntegrityError

from db.models.user import User, UserSettings  
from db.models.profile import Profile
from db.models.conversation import Conversation
from db.models.message import Message
from db.models.match import Match



def test_user_email_unique(session):
    user1 = User(email="a@example.com", username="u1", hashed_password="pwd")
    user2 = User(email="a@example.com", username="u2", hashed_password="pwd")
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()


def test_user_username_unique(session):
    user1 = User(email="a1@example.com", username="same", hashed_password="pwd")
    user2 = User(email="a2@example.com", username="same", hashed_password="pwd")
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()

def test_user_email_non_nullable(session):
    user = User(email=None, username="u", hashed_password="pwd")
    session.add(user)
    with pytest.raises(IntegrityError):
        session.commit()

def test_user_username_non_nullable(session):
    user = User(email="a@example.com", username=None, hashed_password="pwd")
    session.add(user)
    with pytest.raises(IntegrityError):
        session.commit()

def test_user_defaults(session):
    user = User(email="default@example.com", username="u", hashed_password="pwd")
    session.add(user)
    session.commit()
    db_user = session.get(User, user.id)
    assert db_user.is_active is True

def test_user_settings_relationship(session):
    user = User(email="rel@example.com", username="u", hashed_password="pwd")
    session.add(user)
    session.commit()
    
    settings = UserSettings(user_id=user.id)
    session.add(settings)
    session.commit()

    db_user = session.get(User, user.id)
    assert db_user.settings.user_id == user.id
    



