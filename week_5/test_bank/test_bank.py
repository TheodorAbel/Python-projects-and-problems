from bank import value


def test_greet():
    assert value("hello how are you doing?")==0
def test_greet2():
    assert value("Hi how are you doing?")==20
def test_greet3():
    assert value("whats up!.how are you doing?")==100







