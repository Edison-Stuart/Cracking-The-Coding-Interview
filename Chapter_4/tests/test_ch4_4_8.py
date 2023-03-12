'''
Module that tests find_first_common_ancestor function.
'''
import pytest
from ..GraphClasses.graph import build_graph
from ..ch4_4_8 import find_first_common_ancestor

test_data_valid = [
    (
        [
    'my_graph.edges[1].vertices[1].edges[1].vertices[1]',
    'my_graph.edges[1].vertices[1].edges[2].vertices[1].edges[2].vertices[1]'
    ],
    'my_graph.edges[1].vertices[1]'
    ),
    (
        [
    'my_graph.edges[1].vertices[1].edges[1].vertices[1]',
    'my_graph.edges[2].vertices[1].edges[2].vertices[1].edges[2].vertices[1]'
    ],
    'my_graph'
    ),
    (
        [
    'my_graph.edges[1].vertices[1].edges[1].vertices[1]',
    'my_graph.edges[1].vertices[1].edges[1].vertices[1].edges[2].vertices[1]'
    ],
    'my_graph.edges[1].vertices[1]'
    ),
]

@pytest.mark.parametrize("targets,expected", test_data_valid)
def test_find_first_common_ancestor(targets, expected):
    my_graph = build_graph([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    target1 = eval(targets[0])
    target2 = eval(targets[1])
    expected_node = eval(expected)
    result = find_first_common_ancestor(target1, target2)

    assert result == expected_node

test_data_invalid = [
    (
    ['my_graph', 'my_graph.edges[1].vertices[1].edges[1].vertices[1]']
    ),
    (
    ['my_graph.edges[1].vertices[1].edges[1].vertices[1]', 'my_graph']
    ),
    (
    ['my_graph', 'my_graph']
    )
]

@pytest.mark.parametrize("targets", test_data_invalid)
def test_find_first_common_ancestor_error(targets):
    my_graph = build_graph([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    target1 = eval(targets[0])
    target2 = eval(targets[1])

    with pytest.raises(Exception):
        find_first_common_ancestor(target1, target2)
