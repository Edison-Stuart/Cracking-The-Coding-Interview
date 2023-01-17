from ..ch1_1_1 import does_repeat

def test_does_repeat_positive():
    value = does_repeat('abcd')
    assert value is False

def test_does_repeat_negative():
    value = does_repeat('abcdefd')
    assert value is True
