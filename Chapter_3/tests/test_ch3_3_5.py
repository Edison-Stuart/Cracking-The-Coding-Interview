from ch3_3_5 import sort_stack_small_on_top
from data_structures.stack import Stack

def test_sort_stack_small_on_top():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(32)
    my_stack.push(100)
    my_stack.push(0)
    my_stack.push(53)
    my_stack.push(1)
    my_stack.push(10)
    my_stack.push(325)
    my_stack.push(64)
    my_stack.push(102)
    my_stack.push(-1)

    sort_stack_small_on_top(my_stack)

    assert my_stack.pop() == -1
    assert my_stack.pop() == 0
    assert my_stack.pop() == 1
    assert my_stack.pop() == 1
    assert my_stack.pop() == 10
