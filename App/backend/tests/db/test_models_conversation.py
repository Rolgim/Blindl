import uuid

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db.models.conversation import Conversation
from db.models.match import Match
from db.models.message import Message


@pytest.fixture
def conversation_with_messages(session: Session, users_and_matches):
    users = users_and_matches["users"]
    matches = users_and_matches["matches"]

    conversation = Conversation(
        id=uuid.uuid4(),
        match_id=matches["m1"].id,
    )
    session.add(conversation)
    session.commit()

    messages = [
        Message(
            conversation_id=conversation.id,
            sender_id=users["u1"].id,
            content="Hello",
        ),
        Message(
            conversation_id=conversation.id,
            sender_id=users["u2"].id,
            content="Hi!",
        ),
    ]

    session.add_all(messages)
    session.commit()

    return {
        "conversation": conversation,
        "messages": messages,
    }

def test_create_conversation(session, users_and_matches):
    match = users_and_matches["matches"]["m2"]

    conversation = Conversation(
        id=uuid.uuid4(),
        match_id=match.id,
    )
    session.add(conversation)
    session.commit()

    db_conv = session.get(Conversation, conversation.id)
    assert db_conv is not None
    assert db_conv.match_id == match.id

def test_create_conversation(session, users_and_matches):
    match = users_and_matches["matches"]["m2"]

    conversation = Conversation(
        id=uuid.uuid4(),
        match_id=match.id,
    )
    session.add(conversation)
    session.commit()

    db_conv = session.get(Conversation, conversation.id)
    assert db_conv is not None
    assert db_conv.match_id == match.id


def test_unique_conversation_per_match(session, users_and_matches):
    match = users_and_matches["matches"]["m3"]

    c1 = Conversation(id=uuid.uuid4(), match_id=match.id)
    session.add(c1)
    session.commit()

    c2 = Conversation(id=uuid.uuid4(), match_id=match.id)
    session.add(c2)

    with pytest.raises(IntegrityError):
        session.commit()

def test_conversation_messages_relationship(session, conversation_with_messages):
    conversation = conversation_with_messages["conversation"]

    session.refresh(conversation)

    assert len(conversation.messages) == 2
    contents = {m.content for m in conversation.messages}
    assert "Hello" in contents
    assert "Hi!" in contents

def test_delete_conversation_cascades_messages(session, conversation_with_messages):
    conversation = conversation_with_messages["conversation"]
    message_ids = [m.id for m in conversation_with_messages["messages"]]

    session.delete(conversation)
    session.commit()

    for mid in message_ids:
        assert session.get(Message, mid) is None

def test_delete_match_cascades_conversation_and_messages(
    session, conversation_with_messages, users_and_matches
):
    conversation = conversation_with_messages["conversation"]
    messages = conversation_with_messages["messages"]
    match = users_and_matches["matches"]["m1"]
    conversation_id = conversation.id
    message_ids = [m.id for m in messages]

    session.delete(match)
    session.commit()
    session.expunge_all()

    assert session.get(Conversation, conversation_id) is None
    for mid in message_ids:
        assert session.get(Message, mid) is None

