from datetime import date

import pytest
from pydantic import ValidationError

from models.profile.profile_schema import Profile


def test_profile_valid():
    profile = Profile(
        user_id="550e8400-e29b-41d4-a716-446655440000",
        display_name="Test User",
        bio="This is a test bio.",
        birth_date="1990-01-01",
        photos=["http://example.com/photo1.jpg", "http://example.com/photo2.jpg"]
    )
    assert profile.display_name == "Test User"
    assert profile.bio == "This is a test bio."
    assert profile.birth_date == date(1990, 1, 1)

def test_profile_invalid_uuid():
    with pytest.raises(ValidationError):
        Profile(
            user_id="not-a-uuid",
            display_name="Test User"
        )