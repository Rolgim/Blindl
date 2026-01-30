from datetime import date

import pytest
from pydantic import ValidationError

from models.profile.profile_schema import ProfileCreate, ProfileRead, ProfileUpdate


def test_read_profile_valid():
    profile = ProfileCreate(
        display_name="Test User",
        bio="This is a test bio.",
        birth_date="1990-01-01",
        photos=["http://example.com/photo1.jpg", "http://example.com/photo2.jpg"],
        location= "POINT(1 1)"
    )
    assert profile.display_name == "Test User"
    assert profile.bio == "This is a test bio."
    assert profile.birth_date == date(1990, 1, 1)

def test_create_profile_invalid_display_name():
    with pytest.raises(ValidationError):
        ProfileCreate(
            display_name="",
            bio="This is a test bio.",
            birth_date="1990-01-01",
        )
        

def test_create_profile_valid():
    profile = ProfileCreate(
        user_id="550e8400-e29b-41d4-a716-446655440000",
        display_name="Test User",
        bio="This is a test bio.",
        birth_date="1990-01-01",
        photos=["http://example.com/photo1.jpg", "http://example.com/photo2.jpg"],
        location= "POINT(1 1)"
    )
    assert profile.display_name == "Test User"
    assert profile.bio == "This is a test bio."
    assert profile.birth_date == date(1990, 1, 1)

def test_read_profile_invalid_uuid():
    with pytest.raises(ValidationError):
        ProfileRead(
            user_id="not-a-uuid",
            display_name="Test User"
        )


def test_update_profile_valid():
    profile = ProfileUpdate(
        display_name="Test User",
        bio="This is a test bio.",
        birth_date="1990-01-01",
        photos=["http://example.com/photo1.jpg", "http://example.com/photo2.jpg"],
        location= "POINT(1 1)"
    )
    assert profile.display_name == "Test User"
    assert profile.bio == "This is a test bio."
    assert profile.birth_date == date(1990, 1, 1)

def test_update_profile_invalid_display_name():
    with pytest.raises(ValidationError):
        ProfileUpdate(
            display_name="",
            bio="This is a test bio.",
            birth_date="1990-01-01",
        )
        