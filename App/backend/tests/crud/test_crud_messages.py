import uuid

import pytest
from sqlalchemy.orm import Session

from crud.conversation import conversation_crud
from crud.message import message_crud
from db.models.conversation import Conversation
from db.models.message import Message


@pytest.fixture
def conversation(session, users_and_matches):


    match = users_and_matches["matches"]["m1"]

    conv = Conversation(id=uuid.uuid4(), match_id=match.id)
    session.add(conv)
    session.commit()
    session.refresh(conv)
    return conv

def test_create_message(session: Session, conversation, users_and_matches):
    sender = users_and_matches["users"]["u1"]

    msg = message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "Hello world",
        },
    )

    assert msg.id is not None
    assert msg.content == "Hello world"


def test_get_message(session: Session, conversation, users_and_matches):
    sender = users_and_matches["users"]["u1"]

    msg = message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "Ping",
        },
    )

    db_msg = message_crud.get(session, id=msg.id)
    assert db_msg is not None
    assert db_msg.content == "Ping"

def test_get_messages_for_conversation(session, conversation, users_and_matches):
    sender = users_and_matches["users"]["u1"]

    message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "A",
        },
    )
    message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "B",
        },
    )

    messages = message_crud.get_for_conversation(
        session,
        conversation_id=conversation.id,
    )

    assert len(messages) == 2
    assert messages[0].created_at <= messages[1].created_at

def test_delete_message(session, conversation, users_and_matches):
    sender = users_and_matches["users"]["u1"]

    msg = message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "Bye",
        },
    )

    message_crud.delete(session, db_obj=msg)

    assert session.get(Message, msg.id) is None

def test_delete_conversation_cascade_messages(
    session, conversation, users_and_matches
):
    sender = users_and_matches["users"]["u1"]

    msg = message_crud.create(
        session,
        obj_in={
            "conversation_id": conversation.id,
            "sender_id": sender.id,
            "content": "Boom",
        },
    )
    session.commit()

    msg_id = msg.id

    conversation_crud.delete(session, db_obj=conversation)
    session.commit()

    assert session.get(Message, msg_id) is None
