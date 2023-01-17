from operator import is_
from ..ch1_1_2 import is_permutation

def test_is_permutation_true():
    value1 = is_permutation('abc', 'bac')
    value2 = is_permutation('abc', 'abc')
    assert value1 is True
    assert value2 is True

def test_is_permutation_false():
    value1 = is_permutation('abc', 'bbb')
    value2 = is_permutation('abc', 'abca')
    assert value1 is False
    assert value2 is False
