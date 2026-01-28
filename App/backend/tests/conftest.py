import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base


@pytest.fixture(scope="session")
def engine():
    # Base test DB in memory (sqlite)
    engine = create_engine("sqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(engine):
    """Session rollback après chaque test"""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session  

    session.close()
    if transaction.is_active:
        transaction.rollback()
    connection.close()
