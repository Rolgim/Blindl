import pytest
from pydantic import ValidationError

from models.matching.match_decision_schema import MatchDecision


def test_match_decision_valid():
    match_decision = MatchDecision(
        match_id="660e8400-e29b-41d4-a716-446655440000",
        decision="continue"
    )
    assert match_decision.decision.value == "continue"

def test_match_decision_invalid_decision():
    with pytest.raises(ValidationError):
        MatchDecision(
            match_id="660e8400-e29b-41d4-a716-446655440000",
            decision="invalid_decision"
        )