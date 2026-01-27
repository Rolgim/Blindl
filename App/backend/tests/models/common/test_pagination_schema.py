import pytest
from pydantic import ValidationError

from models.common.pagination_schema import Pagination


def test_pagination_defaults():
    p = Pagination()
    assert p.limit is None
    assert p.offset is None

def test_pagination_valid_values():
    p = Pagination(limit=50, offset=10)
    assert p.limit == 50
    assert p.offset == 10

def test_pagination_limit_bounds():
    # limit < 1
    with pytest.raises(ValidationError):
        Pagination(limit=0)
    # limit > 100
    with pytest.raises(ValidationError):
        Pagination(limit=101)

def test_pagination_offset_bounds():
    # offset < 0
    with pytest.raises(ValidationError):
        Pagination(offset=-1)

def test_pagination_optional():
    # only limit provided
    p = Pagination(limit=10)
    assert p.limit == 10
    assert p.offset is None
    # only offset provided
    p = Pagination(offset=5)
    assert p.limit is None
    assert p.offset == 5
