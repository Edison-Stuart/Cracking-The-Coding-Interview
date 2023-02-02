'''Implement a SetOfStacks class that is composed
   of several stacks and creates a new stack once the
   previous one exceeds capacity. push and pop should
   behave the same as a single stack'''

'''
First, we would create a class, SetOfStacks, that accepts
an int value which determines the stack capacity.
The init of the class should also have a top variable,
as well as a stack size variable

	class SetOfStacks:
		__init__(self,stack_capacity):
		    self.stack_capacity = stack_capacity
			self.stack_size = 0
            self.top = None

Then we can implement the push() and pop() methods

For the push method we can check if there is a top node,
if not we push the desired data to the top node and increase our stack size.

	push(self, data):
	    if self.top is None:
            self.top = StackNode(data)
			self.stack_size += 1
            return

if there is a top node we create a new node with the data
and make that the top node, also increasing our stack size

		temp = StackNode(data)
    	temp.next = self.top
        self.top = temp
		self.stack_size += 1

if the stack size modulo the stack capacity is ever 0,
then we create a pointer node that points to the previous head,
as well as new top node on the pointer with our data

    push(self, data):
	    if self.stack_size % self.stack_capacity == 0:
			new_top = StackNode(data)
			pointer = StackNode(Null)
			new_top.next = pointer
			pointer.next = self.top
			self.top = new_top
			self.stack_size += 2

now we can implement the pop method.

for pop() we want to do the same as if it were a normal stack,
however, if we reach a pointer node, whos data is null but has a next value.
we remove the pointer and the node it was pointing to.
we remove 2 from the stack size if this is the case, otherwise just 1

    pop(self):
	    if self.top is None:
            return None
		if self.top.data is None:
			item = self.top.next.data
			self.top = self.top.next.next
			self.stack_size -= 2
			return item

        item = self.top.data
        self.top = self._top.next
		self.stack_size -= 1
        return item
'''
from data_structures.stack import StackNode

class SetOfStacks:
    '''Creates stacks of fixed height based on input'''
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.top = None
        self.stack_size = 0

    def push(self, data):
        if self.top is None:
            self.top = StackNode(data)
            self.stack_size += 1
        elif self.stack_size % self.stack_capacity == 0:
            new_top = StackNode(data)
            pointer = StackNode(None)
            new_top.next = pointer
            pointer.next = self.top
            self.top = new_top
            self.stack_size += 2
        else:
            temp = StackNode(data)
            temp.next = self.top
            self.top = temp
            self.stack_size += 1

    def pop(self):
        if self.top is None:
            item = None
        elif self.top.next.data is None:
            item = self.top.data
            self.top = self.top.next.next
            self.stack_size -= 2
        else:
            item = self.top.data
            self.top = self.top.next
            self.stack_size -= 1
        return item
