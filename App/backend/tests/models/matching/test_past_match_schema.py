import pytest
from pydantic import ValidationError

from models.matching.past_match_schema import PastMatch


def test_past_match_valid():
    past_match = PastMatch(
        match_id="660e8400-e29b-41d4-a716-446655440000",
        profile_id="660e8400-e29b-41d4-a716-446655440001",
        status="accepted",  
        id="550e8400-e29b-41d4-a716-446655440002",
        users=[
            "660e8400-e29b-41d4-a716-446655440001",
            "660e8400-e29b-41d4-a716-446655440002"
        ],
        ended_at="2026-01-27T10:00:00Z",
        outcome="mutual_stop"
    )

    # Assertions
    assert past_match.status.value == "accepted"  # Enum Status from Match
    assert past_match.outcome.value == "mutual_stop"  # Enum Outcome
    assert len(past_match.users) == 2

def test_past_match_invalid_users_length():
    with pytest.raises(ValidationError):
        PastMatch(
            match_id="660e8400-e29b-41d4-a716-446655440000",
            profile_id="660e8400-e29b-41d4-a716-446655440001",
            status="accepted",
            id="550e8400-e29b-41d4-a716-446655440002",
            users=["660e8400-e29b-41d4-a716-446655440001"],  #Only one user instead of two
            ended_at="2026-01-27T10:00:00Z",
            outcome="mutual_stop"
        )

def test_past_match_invalid_outcome():
    with pytest.raises(ValidationError):
        PastMatch(
            match_id="660e8400-e29b-41d4-a716-446655440000",
            profile_id="660e8400-e29b-41d4-a716-446655440001",
            status="accepted",
            id="550e8400-e29b-41d4-a716-446655440002",
            users=[
                "660e8400-e29b-41d4-a716-446655440001",
                "660e8400-e29b-41d4-a716-446655440002"
            ],
            ended_at="2026-01-27T10:00:00Z",
            outcome="not_valid_outcome" 
        )
