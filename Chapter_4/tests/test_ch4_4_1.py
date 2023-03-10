from ..ch4_4_1 import CheckForPath, GraphCycleException
import pytest


@pytest.mark.parametrize("graph, targets, expected",[
    (
    CheckForPath({1: [2, 3], 2: [6], 3: [2, 5], 4: [2], 5: [4], 6: []}),
    [1, 4],
    [1,3,5,4]
	),
    (
    CheckForPath({1: [2, 3], 2: [4], 3: [4], 4: [], 5: [2], 6: [7, 3], 7: [], 8: [6]}),
    [8, 4],
    [8,6,3,4]
	),
])
def test_are_nodes_connected_true(graph, targets, expected):
    response = graph.are_nodes_connected(targets[0], targets[1])
    assert response == expected

@pytest.mark.parametrize("graph, targets, expected",[
    (
    CheckForPath({1: [2, 3], 2: [6], 3: [2, 5], 4: [2], 5: [4], 6: []}),
    [3, 1],
    None
	),
    (
    CheckForPath({1: [2, 3], 2: [4], 3: [4], 4: [], 5: [2], 6: [7, 3], 7: [], 8: [6]}),
    [8, 2],
    None
	),
])
def test_are_nodes_connected_false(graph, targets, expected):
    response = graph.are_nodes_connected(targets[0], targets[1])
    assert response == expected

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
def test_are_nodes_connected_invalid(graph, targets):
    with pytest.raises(Exception):
        graph.are_nodes_connected(targets[0], targets[1])
