# test_seasons.py

import pytest
from datetime import date
from seasons import calculate_minutes_since_birth, convert_minutes_to_words, parse_date

def test_parse_date():
    # Correct date format
    assert parse_date("2023-08-03") == date(2023, 8, 3)

    # Incorrect date format
    with pytest.raises(ValueError):
        parse_date("08-03-2023")  # Wrong format

def test_calculate_minutes_since_birth():

    # Test with a date that includes a leap year
    birth_date = date(2020, 8,  3)
    assert calculate_minutes_since_birth(birth_date) ==2103840

def test_convert_minutes_to_words():
    # Test conversion to words
    assert convert_minutes_to_words(12932640) =="Twelve million, nine hundred thirty-two thousand, six hundred forty"
    assert convert_minutes_to_words(2103840) =="Two million, one hundred three thousand, eight hundred forty"

