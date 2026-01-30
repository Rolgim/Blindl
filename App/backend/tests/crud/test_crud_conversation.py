import uuid

import pytest
from sqlalchemy.orm import Session

from crud.conversation import conversation_crud
from db.models.conversation import Conversation


@pytest.fixture
def conversation(session: Session, users_and_matches):
    match = users_and_matches["matches"]["m1"]

    conv = Conversation(
        id=uuid.uuid4(),
        match_id=match.id,
    )
    session.add(conv)
    session.commit()
    session.refresh(conv)

    return conv

def test_create_conversation(session: Session, users_and_matches):
    match = users_and_matches["matches"]["m2"]

    conv = conversation_crud.create(
        session,
        obj_in={"id": uuid.uuid4(), "match_id": match.id},
    )

    assert conv.id is not None
    assert conv.match_id == match.id

def test_get_conversation(session: Session, conversation):
    db_conv = conversation_crud.get(session, id=conversation.id)

    assert db_conv is not None
    assert db_conv.id == conversation.id

def test_get_conversation_by_match(session: Session, conversation):
    db_conv = conversation_crud.get_by_match_id(
        session,
        match_id=conversation.match_id,
    )

    assert db_conv is not None
    assert db_conv.id == conversation.id

def test_delete_conversation(session: Session, conversation):
    conversation_crud.delete(session, db_obj=conversation)

    db_conv = session.get(Conversation, conversation.id)
    assert db_conv is None

