import os

import pytest
from sqlalchemy import create_engine, text


@pytest.fixture
def db_engine():
    db_url = os.getenv("DATABASE_URL")
    return create_engine(db_url)

def test_mysql_connection_active(db_engine):
    with db_engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        assert result == 1