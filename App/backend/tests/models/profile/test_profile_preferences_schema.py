from datetime import date

import pytest
from pydantic import ValidationError

from models.profile.profile_preferences_schema import (
    ProfilePreferencesCreate,
    ProfilePreferencesUpdate,
    ProfilePreferencesRead,
    GenderPreference
)



def test_create_preferences_valid():
    prefs = ProfilePreferencesCreate(
        min_age=20,
        max_age=30,
        distance_km=10,
        gender_preferences=[GenderPreference.male, GenderPreference.female]
    )
    assert prefs.min_age == 20
    assert prefs.max_age == 30
    assert prefs.distance_km == 10

def test_create_preferences_defaults():
    # Teste que les valeurs par défaut correspondent à celles de la DB
    prefs = ProfilePreferencesCreate()
    assert prefs.min_age == 18
    assert prefs.max_age == 100
    assert prefs.distance_km == 50

def test_update_preferences_partial():
    prefs = ProfilePreferencesUpdate(min_age=25)
    assert prefs.min_age == 25
    assert prefs.max_age is None

def test_read_preferences_from_orm():
    # Simule un objet venant de SQLAlchemy
    class MockDBProfilePreferences:
        min_age = 21
        max_age = 40
        distance_km = 20
        gender_preferences = [] # Note: Assurez-vous que votre modèle DB gère ce champ
    
    db_obj = MockDBProfilePreferences()
    prefs = ProfilePreferencesRead.model_validate(db_obj)
    
    assert prefs.min_age == 21
    assert prefs.max_age == 40
    assert prefs.distance_km == 20

def test_create_preferences_invalid_gender():
    with pytest.raises(ValidationError):
        ProfilePreferencesCreate(
            gender_preferences=["invalid_gender"]
        )
