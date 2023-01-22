from ..ch2_2_3 import delete_middle
from ..linked_list import linked_list

def test_delete_middle_valid1():
    my_list = linked_list.LinkedList(1,2,3,4,5)
    middle_node = my_list.get_specific_node(2)
    delete_middle(middle_node)
    assert my_list.get_all_nodes() == ['1','2','4','5']

def test_delete_middle_valid2():
    my_list = linked_list.LinkedList(1,6,3,8,2,0,155,7,5)
    middle_node = my_list.get_specific_node(6)
    delete_middle(middle_node)
    assert my_list.get_all_nodes() == ['1','6','3','8','2','0','7','5']

def test_delete_middle_node_invalid():
    my_list = linked_list.LinkedList(1,6,3,8,2,0,155,7,5)
    middle_node = my_list.get_specific_node(8)
    assert delete_middle(middle_node) is False
