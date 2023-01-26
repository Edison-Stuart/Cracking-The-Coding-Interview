from ch3_3_3 import SetOfStacks

def test_set_of_stacks_push():
    my_stacks = SetOfStacks(3)
    my_stacks.push(5)
    my_stacks.push(6)
    my_stacks.push(7)
    my_stacks.push(8)
    assert my_stacks.top.data == 8
    assert my_stacks.stack_size == 5

def test_set_of_stacks_pop():
    my_stacks = SetOfStacks(3)
    my_stacks.push(5)
    my_stacks.push(6)
    my_stacks.push(7)
    my_stacks.push(8)

    assert my_stacks.pop() == 8
    assert my_stacks.top.data == 7
    assert my_stacks.stack_size == 3
