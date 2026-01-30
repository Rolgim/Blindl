import pytest
from pydantic import ValidationError

from models.matching.active_match_schema import ActiveMatchRead


def test_read_active_match_valid():
    active_match = ActiveMatchRead(
        match_id="660e8400-e29b-41d4-a716-446655440000",
        profile_id="660e8400-e29b-41d4-a716-446655440001",
        status="accepted",
        id="550e8400-e29b-41d4-a716-446655440002",
        users=[
            "660e8400-e29b-41d4-a716-446655440001",
            "660e8400-e29b-41d4-a716-446655440002"
        ],
        started_at="2026-01-27T10:00:00Z"
    )

    # Assertions
    assert active_match.status.value == "accepted"  # Enum Status from Match
    assert len(active_match.users) == 2

def test_read_active_match_invalid_users_length():
    with pytest.raises(ValidationError):
        ActiveMatchRead(
            match_id="660e8400-e29b-41d4-a716-446655440000",
            profile_id="660e8400-e29b-41d4-a716-446655440001",
            status="accepted",
            id="550e8400-e29b-41d4-a716-446655440002",
            users=["660e8400-e29b-41d4-a716-446655440001"],  #Only one user instead of two
            started_at="2026-01-27T10:00:00Z"
        )