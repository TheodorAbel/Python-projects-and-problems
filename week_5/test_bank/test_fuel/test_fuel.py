import pytest
from fuel import convert, gauge


def test_convert_valid_input():
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("400/400") == 100


def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_valid_input():
    assert gauge(89) == "89%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

