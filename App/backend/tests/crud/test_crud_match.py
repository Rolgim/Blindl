from datetime import datetime

from crud.match import match_crud
from db.models.match import Match, MatchStatus
from db.models.user import User


def test_get_pool_for_user(session):
    user = User(email="u@example.com", username="u", hashed_password="pwd")
    user2 = User(email="u2@example.com", username="u2", hashed_password="pwd")
    user3 = User(email="u3@example.com", username="u3", hashed_password="pwd")
    user4 = User(email="u4@example.com", username="u4", hashed_password="pwd")

    session.add(user)
    session.add(user2)
    session.add(user3)
    session.add(user4)


    session.commit()

    match1 = Match(
        user_a_id=user.id,
        user_b_id=user2.id,
        status=MatchStatus.ACTIVE,
        created_at=datetime(2026, 1, 5),  # week 2
    )
    match2 = Match(
        user_a_id=user.id,
        user_b_id=user3.id,
        status=MatchStatus.ACTIVE,
        created_at=datetime(2026, 1, 6),  # week 2
    )

    match3 = Match(
        user_a_id=user.id,
        user_b_id=user4.id,
        status=MatchStatus.ACTIVE,
        created_at=datetime(2026, 1, 1),  # wrong week (week 1)
    )

    match4 = Match(
        user_a_id=user2.id,
        user_b_id=user4.id,
        status=MatchStatus.ACTIVE,
        created_at=datetime(2026, 1, 6),  # good week but wrong user
    )

    session.add_all([match1, match2, match3, match4])
    session.commit()

    matches = match_crud.get_pool_for_user(
        session,
        user_id=user.id,
        year=2026,
        week=2,
    )

    ids = {m.id for m in matches}
    assert len(matches) == 2
    assert match1.id in ids
    assert match2.id in ids
    assert match3.id not in ids
    assert match4.id not in ids