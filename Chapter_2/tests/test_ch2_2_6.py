from ..ch2_2_6 import linked_list_is_palindrome
from ..linked_list import linked_list

def test_linked_list_is_palindrome_true_even():
    my_list = linked_list.LinkedList(1,2,3,3,2,1)
    value = linked_list_is_palindrome(my_list.head_node)
    assert value is True

def test_linked_list_is_palindrome_true_odd():
    my_list = linked_list.LinkedList(1,2,3,5,3,2,1)
    value = linked_list_is_palindrome(my_list.head_node)
    assert value is True

def test_linked_list_is_palindrome_false_even():
    my_list = linked_list.LinkedList(1,2,3,4,5,6)
    value = linked_list_is_palindrome(my_list.head_node)
    assert value is False

def test_linked_list_is_palindrome_false_odd():
    my_list = linked_list.LinkedList(1,2,3,4,5,6,7)
    value = linked_list_is_palindrome(my_list.head_node)
    assert value is False
