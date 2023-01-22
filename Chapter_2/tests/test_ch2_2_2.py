'''Test file for chapter 2 problem 3, return the kth
   to last element in a singly linked list'''
from ..ch2_2_2 import kth_to_last
from ..linked_list import linked_list

def test_kth_to_last_false():
    my_list = linked_list.LinkedList(1,2,3,4,5,6,7,8,9,10)
    element_index = kth_to_last(my_list.head_node, 11)
    assert element_index == -1

def test_kth_to_last_true():
    my_list = linked_list.LinkedList(1,2,3,4,5,6,7,8,9,10)
    element_index = kth_to_last(my_list.head_node, 6)
	# with index we can easily get the node
    assert element_index == 3
    assert my_list.get_specific_node(element_index).data == 4

def test_kth_to_last_firstEl():
    my_list = linked_list.LinkedList(1,2,3,4,5,6,7,8,9,10)
    element_index = kth_to_last(my_list.head_node, 1)
    assert element_index == 8
    assert my_list.get_specific_node(element_index).data == 9
