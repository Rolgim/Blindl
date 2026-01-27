from datetime import date

import pytest
from pydantic import ValidationError

from models.profile.profile_preferences_schema import ProfilePreferences


def test_profile_preferences_valid():
    profile_preferences = ProfilePreferences(
        age_min=18,
        age_max=99,
        distance_km=10,
        gender_preferences=["male", "female"]
    )
    assert profile_preferences.age_min == 18
    assert profile_preferences.age_max == 99
    assert profile_preferences.distance_km == 10


def test_profile_preferences_invalid_gender():
    with pytest.raises(ValidationError):
        ProfilePreferences(
            gender_preferences=["invalid_gender"]
        )