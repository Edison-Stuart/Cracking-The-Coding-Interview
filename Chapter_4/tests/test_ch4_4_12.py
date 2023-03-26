import pytest
from ..ch4_4_12 import CheckForPath, create_node_list

@pytest.mark.parametrize("target,expected", [(15, [[1, 2, 4, 8], [2, 4, 9], [5, 10], [15]])])
def test_find_all_paths_with_sum(target, expected):
    adjacency_list = create_node_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    my_tree = CheckForPath(adjacency_list)
    assert my_tree.find_paths_with_sum(target) == expected
