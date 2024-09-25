import plates
import pytest

def test_check1():
    assert plates.is_valid("DDF345") == True

def test_check2():
    assert plates.is_valid("Lsd340") == True

def test_check3():
    assert plates.is_valid("mf345") == True

def test_check4():
    assert plates.is_valid("df245") == True

def test_check5():
    assert plates.is_valid("df24as5") == False

def test_check6():
    assert plates.is_valid("a") == False  # Too short

def test_check7():
    assert plates.is_valid("abcd123") == False  # Too long

def test_check8():
    assert plates.is_valid("12ab") == False  # Starts with digits

def test_check9():
    assert plates.is_valid("ab0123") == False  # Leading zero in number part

def test_check10():
    assert plates.is_valid("ab!23") == False  # Contains non-alphanumeric characters

def test_check11():
    assert plates.is_valid("ab12c3") == False  # Letters after digits start
def test_check12():
    assert plates.is_valid("23456")==False
