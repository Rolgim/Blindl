from datetime import datetime

import pytest
from sqlalchemy.orm import Session

from crud.match import match_crud
from db.models.match import Match, MatchStatus
from db.models.user import User


def test_get_for_user(session, users_and_matches):
    users = users_and_matches["users"]
    matches = users_and_matches["matches"]

    result = match_crud.get_for_user(session, user_id=users["u1"].id)
    ids = {m.id for m in result}

    # u1 is in m1, m2, m3, m5
    assert len(result) == 4
    assert matches["m1"].id in ids
    assert matches["m2"].id in ids
    assert matches["m3"].id in ids
    assert matches["m4"].id not in ids
    assert matches["m5"].id in ids


def test_get_active_for_user(session, users_and_matches):
    users = users_and_matches["users"]
    matches = users_and_matches["matches"]

    result = match_crud.get_active_for_user(session, user_id=users["u1"].id)
    ids = {m.id for m in result}

    # u1 is in m1, m2, m3 but not in m5 which is PAST
    assert len(result) == 3
    assert matches["m1"].id in ids
    assert matches["m2"].id in ids
    assert matches["m3"].id in ids
    assert matches["m4"].id not in ids
    assert matches["m5"].id not in ids


def test_get_pool_for_user(session, users_and_matches):
    users = users_and_matches["users"]
    matches = users_and_matches["matches"]

    result = match_crud.get_pool_for_user(session, user_id=users["u1"].id, year=2026, week=2)
    ids = {m.id for m in result}
    # Only m1, m2 and m3 fall into week 2 for u1
    assert len(result) == 3
    assert matches["m1"].id in ids
    assert matches["m2"].id in ids
    assert matches["m3"].id not in ids
    assert matches["m4"].id not in ids
    assert matches["m5"].id in ids


def test_end_match(session, users_and_matches):
    matches = users_and_matches["matches"]
    match_to_end = matches["m1"]

    ended_match = match_crud.end_match(session, match=match_to_end)

    assert ended_match.status == MatchStatus.PAST
    assert ended_match.ended_at is not None


def test_delete_match(session, users_and_matches):
    matches = users_and_matches["matches"]
    match_to_delete = matches["m1"]

    match_crud.delete(session, db_obj=match_to_delete)

    deleted_match = session.get(Match, match_to_delete.id)
    assert deleted_match is None
