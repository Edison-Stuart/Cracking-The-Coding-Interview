import pytest
from ..ch4_4_12 import CheckForPath, create_node_list

@pytest.mark.parametrize(
        "tree_list,target,expected",
        [
            (
                [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
                15,
                [
                    [1, 2, 4, 8],
                    [2, 4, 9],
                    [5, 10],
                    [15]
            ]
        ),
            (
                [20,9,4,13,11,10,30,2,4,10,4,10,-4,-10,-6,9,
                 50,7,36,-6,5,20,-30,96,30,14,19,0,48,103,-4],
                24,
                [
                    [20,4],
                    [4,30,-6,-4],
                    [30,-6],
                    [4,30,-10],
                    [4,30,-10, 0],
                    [4,10,10],
                    [4,10,-4,14],
                    [9,11,4],
                    [9,11,10,-6],
                    [4, 20],
                    [9,13,2],
                    [13,4,7],
                    [13,2,9]
            ]
        )
    ]
)
def test_find_all_paths_with_sum(tree_list, target, expected):
    adjacency_list = create_node_list(tree_list)
    my_tree = CheckForPath(adjacency_list)
    for node in my_tree.find_paths_with_sum(target):
        assert node in expected
