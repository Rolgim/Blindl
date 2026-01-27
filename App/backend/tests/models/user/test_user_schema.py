import pytest
from pydantic import ValidationError

from models.user.user_schema import User


def test_user_valid():
    user = User(
        id="550e8400-e29b-41d4-a716-446655440000",
        email="test@example.com",
        created_at="2026-01-27T09:00:00Z"
    )
    assert user.email == "test@example.com"

def test_user_invalid_uuid():
    with pytest.raises(ValidationError):
        User(
            id="not-a-uuid",
            email="test@example.com",
            created_at="2026-01-27T09:00:00Z"
        )
