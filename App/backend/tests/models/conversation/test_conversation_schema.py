import pytest
from pydantic import ValidationError

from models.conversation.conversation_schema import ConversationCreate, ConversationRead


def test_create_conversation_valid():
    conv = ConversationCreate(
        match_id="770e8400-e29b-41d4-a716-446655440000",
    )
    assert str(conv.match_id) == "770e8400-e29b-41d4-a716-446655440000"

def test_create_conversation_invalid():
    with pytest.raises(ValidationError):
        ConversationCreate(
            match_id="not-a-uuid"
        )

def test_read_conversation_valid():
    conv = ConversationRead(
        id="770e8400-e29b-41d4-a716-446655440000",
        match_id="123e4567-e89b-12d3-a456-426614174000",
        created_at="2023-10-01T12:00:00Z"
    )
    assert str(conv.id) == "770e8400-e29b-41d4-a716-446655440000"
    assert str(conv.match_id) == "123e4567-e89b-12d3-a456-426614174000"
    assert conv.created_at.isoformat() == "2023-10-01T12:00:00+00:00"

def test_read_conversation_invalid():
    with pytest.raises(ValidationError):
        ConversationRead(
            id="not-a-uuid",
            match_id="also-not-a-uuid",
            created_at="invalid-timestamp"
        )