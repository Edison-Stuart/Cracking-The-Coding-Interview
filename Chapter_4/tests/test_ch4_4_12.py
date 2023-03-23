import pytest
from ..ch4_4_12 import CheckForPath

@pytest.mark.parametrize("target,expected", [(15, [[1, 2, 4, 8], [2, 4, 9], [5, 10], [15]])])
def test_find_all_paths_with_sum(target, expected):
    adjacency_list = {
        1: [2,3],
        2: [4,5],
        3: [6,7],
		4: [8,9],
		5: [10,11],
		6: [12, 13],
		7: [14, 15],
		8: [16],
		9: [],
		10: [],
		11: [],
		12: [],
		13: [],
        14: [],
        15: [],
        16: []
        }
    my_tree = CheckForPath(adjacency_list)
    assert my_tree.find_paths_with_sum(target) == expected
