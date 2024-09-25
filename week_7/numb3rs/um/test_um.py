import pytest
from um import count


def test_count():
    assert count("Hello UM world")==1
    assert count("um is there um anything new?")==2
    assert count("yummy")==0
    

