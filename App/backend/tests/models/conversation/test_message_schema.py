import pytest
from pydantic import ValidationError

from models.conversation.message_schema import Message


def test_message_valid():
    msg = Message(
        id="880e8400-e29b-41d4-a716-446655440000",
        conversation_id="770e8400-e29b-41d4-a716-446655440000",
        sender_id="990e8400-e29b-41d4-a716-446655440000",
        content="Hello world!",
        sent_at="2026-01-27T10:05:00Z"
    )
    assert str(msg.id.root) == "880e8400-e29b-41d4-a716-446655440000"
    assert str(msg.conversation_id.root) == "770e8400-e29b-41d4-a716-446655440000"


def test_message_invalid_content():
    with pytest.raises(ValidationError):
        Message(
            id="880e8400-e29b-41d4-a716-446655440000",
            conversation_id="770e8400-e29b-41d4-a716-446655440000",
            sender_id="990e8400-e29b-41d4-a716-446655440000",
            content="x" * 3000,  # dépasse max_length=2000
            sent_at="2026-01-27T10:05:00Z"
        )