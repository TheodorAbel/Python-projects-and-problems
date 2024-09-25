import pytest
from working import convert

def test_valid_conversion():

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_format():

    with pytest.raises(ValueError):
        convert("9 to 5 PM")  # Missing AM/PM for the first time
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")  # Missing "to" keyword
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Incorrect delimiter instead of "to"
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:00 AM")  # Invalid minute value
   
