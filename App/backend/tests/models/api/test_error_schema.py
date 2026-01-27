import pytest
from pydantic import ValidationError

from models.api.error_schema import Error


def test_error_valid():
    err = Error(code="404", message="Not found")
    assert err.code == "404"
    assert err.message == "Not found"

def test_error_missing_field():
    with pytest.raises(ValidationError):
        Error(code="500")  