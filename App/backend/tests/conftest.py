import os  # noqa: I001

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime

from db.base import Base
from db.models.match import Match, MatchStatus
from db.models.user import User


@pytest.fixture(scope="session")
def engine():
    database_url = os.environ["DATABASE_URL"]

    engine = create_engine(
        database_url,
        echo=False,
        future=True,
    )

    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield engine

    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope="function")
def session(engine):
    """Session rollback after testing"""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session  

    session.close()
    if transaction.is_active:
        transaction.rollback()
    connection.close()

@pytest.fixture
def users_and_matches(session: Session):
    users = {
        "u1": User(email="u@example.com", username="u", hashed_password="pwd"),
        "u2": User(email="u2@example.com", username="u2", hashed_password="pwd"),
        "u3": User(email="u3@example.com", username="u3", hashed_password="pwd"),
        "u4": User(email="u4@example.com", username="u4", hashed_password="pwd"),
        "u5": User(email="u5@example.com", username="u5", hashed_password="pwd"),
    }
    session.add_all(users.values())
    session.commit()

    matches = {
        "m1": Match(
            user_a_id=users["u1"].id,
            user_b_id=users["u2"].id,
            status=MatchStatus.ACTIVE,
            created_at=datetime(2026, 1, 5),
        ),
        "m2": Match(
            user_a_id=users["u1"].id,
            user_b_id=users["u3"].id,
            status=MatchStatus.ACTIVE,
            created_at=datetime(2026, 1, 6),
        ),
        "m3": Match(
            user_a_id=users["u1"].id,
            user_b_id=users["u4"].id,
            status=MatchStatus.ACTIVE,
            created_at=datetime(2026, 1, 1),
        ),
        "m4": Match(
            user_a_id=users["u2"].id,
            user_b_id=users["u4"].id,
            status=MatchStatus.ACTIVE,
            created_at=datetime(2026, 1, 6),
        ),
        "m5": Match(
            user_a_id=users["u1"].id,
            user_b_id=users["u5"].id,
            status=MatchStatus.PAST,
            created_at=datetime(2026, 1, 6),
        ),
    }

    session.add_all(matches.values())
    session.commit()

    return {"users": users, "matches": matches}
