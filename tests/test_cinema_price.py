import pytest
from src.cinema_price import ticket_price

# ---------- Valid inputs ----------

def test_multiple_tickets_total():  # CIN-PRC-TC-001
    result = ticket_price(3)
    assert result == 3600
    assert type(result) is int

def test_one_ticket_costs_1200():  # CIN-PRC-TC-002
    assert ticket_price(1) == 1200

def test_zero_tickets_cost_zero():  # CIN-PRC-TC-003
    assert ticket_price(0) == 0

def test_large_number_of_tickets():  # CIN-PRC-TC-004
    assert ticket_price(1000) == 1200000

# ---------- Invalid range ----------

def test_negative_ticket_count_rejected():  # CIN-PRC-TC-005
    with pytest.raises(ValueError):
        ticket_price(-1)

# ---------- Invalid type ----------

def test_string_ticket_count_rejected():  # CIN-PRC-TC-006
    with pytest.raises(TypeError):
        ticket_price("3")

@pytest.mark.parametrize("value", [2.5, 3.0])
def test_float_ticket_count_rejected(value):  # CIN-PRC-TC-007
    with pytest.raises(TypeError):
        ticket_price(value)

def test_none_ticket_count_rejected():  # CIN-PRC-TC-008
    with pytest.raises(TypeError):
        ticket_price(None)

@pytest.mark.parametrize("value", [True, False])
def test_boolean_ticket_count_rejected(value):  # CIN-PRC-TC-009
    with pytest.raises(TypeError):
        ticket_price(value)