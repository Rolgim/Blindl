import pytest
from pydantic import ValidationError

from models.api.error_schema import Error
from models.api.response_schema import Response


def test_response_with_data():
    resp = Response(data={"user": "Alice"})
    assert resp.data == {"user": "Alice"}
    assert resp.error is None

def test_response_with_error():
    err = Error(code="400", message="Bad request")
    resp = Response(error=err)
    assert resp.data is None
    assert resp.error.code == "400"
    assert resp.error.message == "Bad request"

def test_response_invalid_error():
    with pytest.raises(ValidationError):
        Response(error={"code": "500"}) 
