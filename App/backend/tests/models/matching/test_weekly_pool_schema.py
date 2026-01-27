import pytest
from pydantic import ValidationError

from models.matching.match_schema import Match
from models.matching.weekly_pool_schema import WeeklyPool


def test_weekly_pool_valid():
    weekly_pool = WeeklyPool(
        user_id="770e8400-e29b-41d4-a716-446655440000",
        week="2026-W04",
        matches=[
            Match(
                match_id="660e8400-e29b-41d4-a716-446655440000",
                profile_id="660e8400-e29b-41d4-a716-446655440001",
                status="accepted"
            )
        ]
    )
    assert weekly_pool.week == "2026-W04"
    assert weekly_pool.matches[0].status.value == "accepted"


def test_weekly_pool_invalid():
    with pytest.raises(ValidationError):
        WeeklyPool(
            id="not-a-uuid",
            week_start="2026-01-26",
            matches=[]
        )