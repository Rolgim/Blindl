import pytest
from pydantic import ValidationError

from models.matching.match_schema import MatchRead, MatchUpdate


def test_read_match_valid():
    match = MatchRead(
        match_id="660e8400-e29b-41d4-a716-446655440000",
        profile_id="660e8400-e29b-41d4-a716-446655440001",
        status="accepted"
    )
    assert match.status.value == "accepted"
    
def test_read_match_invalid_uuid():
    with pytest.raises(ValidationError):
        MatchRead(
            match_id="not-a-uuid",
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            status="accepted"
        )

def test_read_match_invalid_status():
    with pytest.raises(ValidationError):
        MatchRead(
            match_id="not-a-uuid",
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            status="notastatus"
        )

def test_update_match_valid_status():
    with pytest.raises(ValidationError):
        MatchRead(
            match_id="660e8400-e29b-41d4-a716-446655440000",
            status="rejected"
        )    
def test_update_match_invalid_status():
    with pytest.raises(ValidationError):
        MatchRead(
            match_id="not-a-uuid",
            status="notastatus"
        )    