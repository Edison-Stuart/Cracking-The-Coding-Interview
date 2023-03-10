from ..ch4_4_1 import CheckForPath
import pytest

@pytest.mark.parametrize("graph, targets, expected",[
    (
    CheckForPath({1: [2, 3], 2: [6], 3: [2, 5], 4: [2], 5: [4], 6: []}),
    [1, 4],
    True
	),
    (
    CheckForPath({1: [2, 3], 2: [4], 3: [4], 4: [], 5: [2], 6: [7, 3], 7: [], 8: [6]}),
    [8, 4],
    True
	),
])
def test_find_any_path_true(graph, targets, expected):
    response = graph.is_path_present(targets[0], targets[1])
    assert response is expected

@pytest.mark.parametrize("graph, targets, expected",[
    (
    CheckForPath({1: [2, 3], 2: [6], 3: [2, 5], 4: [2], 5: [4], 6: []}),
    [3, 1],
    False
	),
    (
    CheckForPath({1: [2, 3], 2: [4], 3: [4], 4: [], 5: [2], 6: [7, 3], 7: [], 8: [6]}),
    [8, 2],
    False
	),
])
def test_find_any_path_false(graph, targets, expected):
    response = graph.is_path_present(targets[0], targets[1])
    assert response is expected

@pytest.mark.parametrize("graph, targets",[
    (
    CheckForPath({1: [2, 3], 2: [6, 1], 3: [2, 5], 4: [2], 5: [4], 6: []}),
    [1, 5]
	),
    (
    CheckForPath({1: [2, 3], 2: [4], 3: [4, 8], 4: [], 5: [2], 6: [7, 3], 7: [], 8: [6]}),
    [8, 2]
	),
])
def test_find_any_path_invalid(graph, targets):
    with pytest.raises(Exception):
        graph.is_path_present(targets[0], targets[1])
