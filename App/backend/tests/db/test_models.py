# tests/db/test_models.py
import pytest  # noqa: I001
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from db.base import Base
from db.models.user import User, UserSettings  
from db.models.profile import Profile


# Tests CRUD User
def test_create_user(session):
    user = User(email="test@example.com", username="testuser", hashed_password="hashed")
    session.add(user)
    session.commit()

    assert user.id is not None
    db_user = session.get(User, user.id)
    assert db_user.email == "test@example.com"
    assert db_user.username == "testuser"


def test_unique_user_email(session):
    user1 = User(email="unique@example.com", username="u1", hashed_password="pwd")
    user2 = User(email="unique@example.com", username="u2", hashed_password="pwd")
    session.add(user1)
    session.commit()

    session.add(user2)
    with pytest.raises(IntegrityError):
        session.commit()


# Tests UserSettings
def test_user_settings_link(session):
    user = User(email="user2@example.com", username="user2", hashed_password="pwd")
    session.add(user)
    session.commit()

    settings = UserSettings(user_id=user.id, language="en", email_notifications=True, weekly_pool_enabled=False)
    session.add(settings)
    session.commit()

    db_settings = session.get(UserSettings, user.id)
    assert db_settings.user_id == user.id
    assert db_settings.language == "en"


# Tests Profile 
def test_create_profile(session):
    user = User(email="profileuser@example.com", username="profileuser", hashed_password="pwd")
    session.add(user)
    session.commit()

    profile = Profile(
        user_id=user.id,
        display_name="Test Profile",
        bio="Hello",
        birth_date=date(1990, 1, 1)
    )
    session.add(profile)
    session.commit()

    assert profile.user_id is not None
    db_profile = session.get(Profile, profile.user_id)
    assert db_profile.bio == "Hello"
    assert db_profile.birth_date == date(1990, 1, 1)    