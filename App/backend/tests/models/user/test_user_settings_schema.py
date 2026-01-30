import pytest
from pydantic import ValidationError

from models.user.user_settings_schema import UserSettingsCreate, UserSettingsUpdate, UserSettingsRead


def test_create_user_settings_valid():
    user_settings = UserSettingsCreate(
        language="en",
        email_notifications=False,
        weekly_pool_enabled=True
    )
    assert user_settings.language == "en"
    assert user_settings.email_notifications is False
    assert user_settings.weekly_pool_enabled is True

def test_create_user_settings_invalid():
    with pytest.raises(ValidationError):
        UserSettingsCreate(
            language=123,  # Invalid type
            email_notifications="yes",  # Invalid type
            weekly_pool_enabled=None  # Valid
        )

def test_update_user_settings_valid():
    user_settings = UserSettingsUpdate(
        language="en",
        email_notifications=False,
        weekly_pool_enabled=True
    )
    assert user_settings.language == "en"
    assert user_settings.email_notifications is False
    assert user_settings.weekly_pool_enabled is True

def test_update_user_settings_invalid():
    with pytest.raises(ValidationError):
        UserSettingsUpdate(
            language=123,  # Invalid type
            email_notifications="yes",  # Invalid type
            weekly_pool_enabled=None  # Valid
        )

def test_read_user_settings_valid():
    user_settings = UserSettingsRead(
        language="en",
        email_notifications=False,
        weekly_pool_enabled=True
    )
    assert user_settings.language == "en"
    assert user_settings.email_notifications is False
    assert user_settings.weekly_pool_enabled is True

def test_read_user_settings_invalid():
    with pytest.raises(ValidationError):
        UserSettingsRead(
            language=123,  # Invalid type
            email_notifications="yes",  # Invalid type
            weekly_pool_enabled=None  # Valid
        )
