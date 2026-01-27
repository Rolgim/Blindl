from datetime import datetime

import pytest
from pydantic import ValidationError

from models.common.timestamp_schema import Timestamp


def test_valid_timestamp():
    ts = Timestamp(root="2023-10-01T12:34:56Z") 
    assert ts.root == datetime(2023, 10, 1, 12, 34, 56, tzinfo=ts.root.tzinfo)

def test_invalid_timestamp_format():
    with pytest.raises(ValidationError) as exc_info:
        Timestamp(timestamp="2023/10/01 12:34:56")
    assert "timestamp" in str(exc_info.value)

def test_empty_timestamp():
    with pytest.raises(ValidationError) as exc_info:
        Timestamp(timestamp="")
    assert "timestamp" in str(exc_info.value)
