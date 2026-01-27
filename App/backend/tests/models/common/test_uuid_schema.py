import pytest
from pydantic import ValidationError

from models.common.uuid_schema import Uuid

def test_uuid_valid():
    uuid_instance = Uuid(root="550e8400-e29b-41d4-a716-446655440000")
    assert str(uuid_instance.root) == "550e8400-e29b-41d4-a716-446655440000"

def test_uuid_invalid():
    with pytest.raises(ValidationError):
        Uuid(root="not-a-uuid")

def test_uuid_empty():
    with pytest.raises(ValidationError):
        Uuid(root="")
