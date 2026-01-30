import pytest
from pydantic import ValidationError

from models.matching.match_schema import MatchRead
from models.matching.weekly_pool_schema import WeeklyPoolRead, WeeklyPoolUpdate


def test_read_weekly_pool_valid():
    weekly_pool = WeeklyPoolRead(
        user_id="770e8400-e29b-41d4-a716-446655440000",
        week="2026-W04",
        matches=[
            MatchRead(
                match_id="660e8400-e29b-41d4-a716-446655440000",
                profile_id="660e8400-e29b-41d4-a716-446655440001",
                status="accepted"
            )
        ]
    )
    assert weekly_pool.week == "2026-W04"
    assert weekly_pool.matches[0].status.value == "accepted"


def test_read_weekly_pool_invalid():
    with pytest.raises(ValidationError):
        WeeklyPoolRead(
            id="not-a-uuid",
            week_start="2026-01-26",
            matches=[]
        )


def test_update_weekly_pool_valid():
    weekly_pool = WeeklyPoolUpdate(
        user_id="770e8400-e29b-41d4-a716-446655440000",
        week="2026-W04",
        matches=[
            MatchRead(
                match_id="660e8400-e29b-41d4-a716-446655440000",
                profile_id="660e8400-e29b-41d4-a716-446655440001",
                status="accepted"
            ),
            MatchRead(
                match_id="660e8400-e29b-41d4-a716-446655440020",
                profile_id="660e8400-e29b-41d4-a716-446655443001",
                status="accepted"
            )
        ]
    )
    assert weekly_pool.week == "2026-W04"
    assert weekly_pool.matches[0].status.value == "accepted"


def test_update_weekly_pool_invalid():
    with pytest.raises(ValidationError):
        WeeklyPoolUpdate(
            user_id="770e8400-e29b-41d4-a716-446655440000",
            week="2026-W04",
            matches=[]
        )

