import pytest
from src.cinema_entry import can_watch

# ---------- Valid inputs ----------

def test_adult_is_allowed():  # CIN-ENT-TC-001
    assert can_watch(20) is True

def test_age_15_is_not_allowed():  # CIN-ENT-TC-002
    assert can_watch(15) is False

def test_age_16_is_allowed():  # CIN-ENT-TC-003
    assert can_watch(16) is True

def test_age_17_is_allowed():  # CIN-ENT-TC-004
    assert can_watch(17) is True

def test_age_zero_is_not_allowed():  # CIN-ENT-TC-005
    assert can_watch(0) is False

# ---------- Invalid range ----------

def test_negative_age_rejected():  # CIN-ENT-TC-006
    with pytest.raises(ValueError):
        can_watch(-1)

# ---------- Invalid type ----------

def test_string_age_rejected():  # CIN-ENT-TC-007
    with pytest.raises(TypeError):
        can_watch("16")

@pytest.mark.parametrize("value", [16.5, 16.0])
def test_float_age_rejected(value):  # CIN-ENT-TC-008
    with pytest.raises(TypeError):
        can_watch(value)

def test_none_age_rejected():  # CIN-ENT-TC-009
    with pytest.raises(TypeError):
        can_watch(None)

@pytest.mark.parametrize("value", [True, False])
def test_boolean_age_rejected(value):  # CIN-ENT-TC-010
    with pytest.raises(TypeError):
        can_watch(value)