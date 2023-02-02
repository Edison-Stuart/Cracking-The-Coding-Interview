from ch3_3_1 import ArrayOfStacks
import pytest

def test_array_of_stacks_push_overload():
    my_stack = ArrayOfStacks(10)
    for _ in range(3):
        for i in range(3):
            my_stack.push(i*2, i + 1)
    my_stack.push(10, 1)
    with pytest.raises(MemoryError):
        my_stack.push(15, 2)

def test_array_of_stacks_push_shift_middle_right():
    my_stack = ArrayOfStacks(10)
    for _ in range(3):
        for i in range(3):
            my_stack.push(i*2, i + 1)
    assert my_stack.stack == [0, 0, 0, None, 2, 2, 2, 4, 4, 4]
    my_stack.push(15, 1)
    assert my_stack.stack == [0, 0, 0, 15, 2, 2, 2, 4, 4, 4]

def test_array_of_stacks_push_shift_middle_left():
    my_stack = ArrayOfStacks(10)
    for _ in range(3):
        for i in range(3):
            my_stack.push(i*2, i + 1)
    assert my_stack.stack == [0, 0, 0, None, 2, 2, 2, 4, 4, 4]
    my_stack.push(15, 3)
    assert my_stack.stack == [0, 0, 0, 2, 2, 2, 15, 4, 4, 4]

def test_array_of_stacks_pop_and_peek():
    my_stack = ArrayOfStacks(10)
    my_stack.push(10, 1)
    my_stack.push(11, 1)

    my_stack.push(15, 2)
    my_stack.push(16, 2)

    my_stack.push(20, 3)
    my_stack.push(21, 3)

    peeked_values = [my_stack.peek(1), my_stack.peek(2), my_stack.peek(3)]
    popped_values = [my_stack.pop(1), my_stack.pop(2), my_stack.pop(3)]
    re_peeked_values = [my_stack.peek(1), my_stack.peek(2), my_stack.peek(3)]

    assert popped_values == peeked_values
    assert re_peeked_values == [10, 15, 20]
