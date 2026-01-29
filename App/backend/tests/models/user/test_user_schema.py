import pytest
from pydantic import ValidationError

from models.user.user_schema import UserCreate, UserRead


def test_create_user_valid():
    user = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    assert user.email == "test@example.com"

def test_create_user_invalid_username():
    with pytest.raises(ValidationError):
        UserCreate(
            email="test@example.com",
            username= None,
            password= "testpassword"
        )

def test_read_user_valid():
    user = UserRead(
        id ="880e8400-e29b-41d4-a716-446655440000",
        email="test@example.com",
        username="testuser",
        is_active=True,
        created_at="2026-01-27T10:05:00Z"
    )
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.is_active is True


def test_read_user_invalid_id():
    with pytest.raises(ValidationError):
        UserRead(
        id ="invalid",
        email="test@example.com",
        username="testuser",
        is_active=True,
        created_at="2026-01-27T10:05:00Z"
        )
