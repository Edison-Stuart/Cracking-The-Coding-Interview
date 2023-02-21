from ..ch4_4_3 import tree_to_linked_lists
from ..TreeClasses.tree_node import build_tree

def test_tree_to_linked_lists():
    head_node = build_tree([50,30,70,20,40,60,80,10,25])
    linked_lists = tree_to_linked_lists(head_node)

    assert len(linked_lists) == 4

    list1 = linked_lists[1]
    list2 = linked_lists[2]
    list3 = linked_lists[3]
    list4 = linked_lists[4]

    assert list1.data == 10
    assert list1.next_node.data == 25
    assert list1.next_node.next_node is None

    assert list2.data == 20
    assert list2.next_node.data == 40
    assert list2.next_node.next_node.data == 60
    assert list2.next_node.next_node.next_node.data == 80
    assert list2.next_node.next_node.next_node.next_node is None

    assert list3.data == 30
    assert list3.next_node.data == 70
    assert list3.next_node.next_node is None

    assert list4.data == 50
    assert list4.next_node is None
