import pytest
from pydantic import ValidationError

from models.user.user_settings_schema import UserSettings


def test_user_settings_valid():
    user_settings = UserSettings(
        language="en",
        email_notifications=False,
        weekly_pool_enabled=True
    )
    assert user_settings.language == "en"
    assert user_settings.email_notifications is False
    assert user_settings.weekly_pool_enabled is True

def test_user_settings_invalid():
    with pytest.raises(ValidationError):
        UserSettings(
            language=123,  # Invalid type
            email_notifications="yes",  # Invalid type
            weekly_pool_enabled=None  # Valid, but let's test the others
        )
