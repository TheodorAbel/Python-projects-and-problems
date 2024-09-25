from twttr import shorten


def test_shorten():

    assert shorten("hEllo")=="hll"
    assert shorten("what's up? 4")=="wht's p? 4"







