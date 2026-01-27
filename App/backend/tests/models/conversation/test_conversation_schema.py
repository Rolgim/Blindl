import pytest
from pydantic import ValidationError

from models.conversation.conversation_schema import Conversation

def test_conversation_valid():
    conv = Conversation(
        id="770e8400-e29b-41d4-a716-446655440000",
        match_id="660e8400-e29b-41d4-a716-446655440000",
        created_at="2026-01-27T10:00:00Z"
    )
    assert str(conv.id.root) == "770e8400-e29b-41d4-a716-446655440000"
    assert str(conv.match_id.root) == "660e8400-e29b-41d4-a716-446655440000"

def test_conversation_invalid_uuid():
    with pytest.raises(ValidationError):
        Conversation(
            id="not-a-uuid",
            match_id="660e8400-e29b-41d4-a716-446655440000",
            created_at="2026-01-27T10:00:00Z"
        )