import pytest
from ..ch10_10_3 import search_rotated_list

@pytest.mark.parametrize('list, target, expected', [
    (
        [15, 18, 20, 26, 30, 1, 4, 7, 10, 13],
        10,
        8
    ),
    (
        [4, 5, 6, 7, 0, 1, 2],
        0,
        4
    ),
    (
        [15, 18, 20, 26, 30, 1, 4, 7, 10, 13],
        2,
        -1
    ),
    (
        [4, 5, 6, 7, 0, 1, 2],
        3,
        -1
    )
])
def search_rotated_list(my_list, target, expected):
    assert search_rotated_list(target, my_list) == expected
