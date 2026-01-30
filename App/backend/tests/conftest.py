import os

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from db.base import Base


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
