import pytest
from jar import Jar

def test_init():
    # Test valid initialization
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test invalid initialization
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("invalid")

def test_str():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(3)
def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_capacity():
    jar = Jar(15)
    assert jar.capacity == 15

def test_size():
    jar = Jar(5)
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1
