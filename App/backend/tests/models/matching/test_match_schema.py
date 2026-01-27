import pytest
from pydantic import ValidationError

from models.matching.match_schema import Match


def test_match_valid():
    match = Match(
        match_id="660e8400-e29b-41d4-a716-446655440000",
        profile_id="660e8400-e29b-41d4-a716-446655440001",
        status="accepted"
    )
    assert match.status.value == "accepted"
    
def test_match_invalid_uuid():
    with pytest.raises(ValidationError):
        Match(
            match_id="not-a-uuid",
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            status="accepted"
        )