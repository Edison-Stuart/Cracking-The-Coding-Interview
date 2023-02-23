from ..ch4_4_3 import tree_to_linked_lists
from ..TreeClasses.tree_node import build_tree
from ..linked_list.list_node import Node

def test_tree_to_linked_lists():
    head_node = build_tree([50,30,70,20,40,60,80,10,25])
    linked_lists = tree_to_linked_lists(head_node)

    assert len(linked_lists) == 4

    for linked_list in linked_lists:
        assert isinstance(linked_list, Node)

    assert linked_lists[0].data == 50
    assert linked_lists[0].next_node is None

    assert linked_lists[1].data == 30
    assert linked_lists[1].next_node.data == 70
    assert linked_lists[1].next_node.next_node is None

    assert linked_lists[2].data == 20
    assert linked_lists[2].next_node.data == 40
    assert linked_lists[2].next_node.next_node.data == 60
    assert linked_lists[2].next_node.next_node.next_node.data == 80
    assert linked_lists[2].next_node.next_node.next_node.next_node is None

    assert linked_lists[3].data == 10
    assert linked_lists[3].next_node.data == 25
    assert linked_lists[3].next_node.next_node is None
