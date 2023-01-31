'''Describe how you could use a single array to implement three stacks'''

'''
In order to imlement three stacks in one array,
lets think about how to implement just one stack in a fixed amount of space.

lets make a class called StackArray

	class StackArray {



In this class we want to store the head of the stack in a variable,
and create an array that will be our stack. We can have this array be of variable
size but for now lets just say it is of size 10. We also want to accept
the size the stack should be.

	constructor(stack_size) {
		self.stack = [null] * 10
		self.head = null
		self.stack_size = stack_size
	}

First lets implement the push method.
What we want to do is check the self.head pointer
and see if it is null. if it is then we take the data
and append it to the array.

	push(data){
		if (self.head == null) {
			self.stack.append(data)
		}
	}

If the head is not null we first check if head + 1 == self.stack_size,
if it is, we return a notice saying that the stack is at the size limit.
If the head is not yet at the stack size,
we go to the index head + 1 and insert the data there as well as increase the
head by 1

	if (self.head == null) {
		self.stack.append(data)
	} else {
		if self.head + 1 == self.stack_size {
			return "stack at size limit"
		}
		self.stack.insert(head + 1, data)
		self.head += 1
	}

Now we can implement the pop method.
for the pop method we first check that self.head is not null,
if it is then we return a notice saying that the stack is empty.
if not then we simply save the value at index head, then set
self.stack[index] equal to null.
There is also the case of the last element being removed.
if self.head == 0 then we go through the same steps as before,
with the added step of setting self.head = null.

	pop() {
		if (self.head == null) {
			return "stack is empty"
		}
		value = self.stack[self.head]
		self.stack[self.head] = null
		if (self.head == 0) {
			self.head = null
		} elif (self.head > 0) {
			self.head -= 1
		}
		return value
	}
}
///////////////////////////////////////////////////////////
So, Now that we have done it for one stack, lets try it with two.

for our constructor we would want to accept the same data, however
instead of self.head we now want to store self.head_1 and self.head_2.

	constructor(stack_size) {
		self.stack = [null] * 10
		self.head_1 = null
		self.head_2 = null
		self.stack_size = stack_size
	}

now in our push method, we want to accept a 1 or 2,
for stack 1 or stack 2. if stack == 1, we do the same as if it
were just one stack. if stack == 2, we have to work our way backwards
from the end of the stack.
we can also break these two operations up into two
functions

	push(data, stack) {
		if (stack == 1) {
			self._pushToFrontStack(data)
		} elif (stack == 2) {
			self._pushToBackStack(data)
		} else {
			raise Exception("value 'stack' should be 1 or 2")
		}
	}

as mentioned before, pushing to the frunt stack will be
the same as before.
	_pushToFrontStack(data) {
		if (self.head_1 is None){
            self.stack.append(data)
            self.head_1 = 0
			}
        else {
            if (self.head_1 + 1 == self.stack_size) {
                raise Exception("stack 1 at capacity")
			}
            self.stack.insert(self.head_1 + 1, data)
            self.head_1 += 1
			}
	}

to push to the back stack, we want to make the same check on the head as before,
but instead of setting it to 0 if null, we set it to len(self.stack) - 1

For the stack size check, we will take the value of
len(self.stack) - (self.head_2) and see if that is equal to the stack_size.
then we insert our data at self.stack[head_2 + 1] and lower head_2 by 1

	_pushToBackStack(data) {
		if (self.head_2 == null) {
            self.head_2 = len(self.stack) - 1
            self.stack.insert(self.head_2, data)
		} else {
			if ((len(self.stack) - self.head_2) == self.stack_size) {
				raise Exception("stack 2 is at capacity)
			}
			self.stack.insert(self.head_2 - 1, data)
			self.head_2 -= 1
		}

Now for the pop method we have to do a similar thing.

	pop(stack) {
		if (stack == 1) {
			self._popFromFrontStack()
		} elif (stack == 2) {
			self._popFromBackStack()
		} else {
			raise Exception("value 'stack' should be 1 or 2")
		}
	}

popFromFrontStack will do the same thing as if it were one stack

	_popFromFrontStack() {
		if (self.head_1 == null) {
            raise Exception("stack 1 is empty")
		}
        value = self.stack[self.head_1]
        self.stack[self.head_1] = null
        if (self.head_1 == 0) {
            self.head_1 = null
        }
		elif (self.head_1 > 0) {
            self.head -= 1
		}
        return value
	}

popFromBackStack will mirror popFromFrontStack
	_popFromBackStack() {
		if (self.head_2 == null) {
			raise Exception("Stack 2 is empty")
		}
		value = self.stack[self.head_2]
		self.stack[self.head_2] = null
		if (self.head_2 == len(self.stack) - 1) {
			self.head_2 = null
		} elif (self.head_2 < len(self.stack) - 1) {
			self.head_2 += 1
		}
	}

We will call this modified calss ArrayOfStacks

	}
'''
class ArrayOfStacks:
    '''A class that uses an array which stores a stack in a subset of the array'''
    def __init__(self, stack_size):
        '''Accepts size limit of stack, no greater than 9'''
        self.stack = [None] * 10
        self.head_1 = None
        self.head_2 = None
        self.stack_size = stack_size

    def push(self, data, stack):
        '''Accepts data and then which stack, 1 or 2, to
		   push the data to'''
        if stack == 1:
            self._push_to_front_stack(data)
        elif stack == 2:
            self._push_to_back_stack(data)
        else:
            raise Exception("value 'stack' should be 1 or 2")

    def pop(self, stack):
        '''Accepts a stack number, 1 or 2, and pops out
		   the top value from that stack'''
        value = None
        if stack == 1:
            value = self._pop_from_front_stack()
        elif stack == 2:
            value = self._pop_from_back_stack()
        else:
            raise Exception("value 'stack' should be 1 or 2")
        return value

    def _push_to_front_stack(self, data):
        '''Takes data and puts it into stack 1'''
        if self.head_1 is None:
            self.head_1 = 0
            self.stack[self.head_1] = data
        else:
            if self.head_1 + 1 == self.stack_size:
                raise Exception("stack 1 at capacity")
            self.head_1 += 1
            self.stack[self.head_1] = data

    def _push_to_back_stack(self, data):
        '''Takes data and puts it into stack 2'''
        if self.head_2 is None:
            self.head_2 = len(self.stack) - 1
            self.stack[self.head_2] = data
        else:
            if (len(self.stack) - self.head_2) == self.stack_size:
                raise Exception("stack 2 is at capacity")
            self.head_2 -= 1
            self.stack[self.head_2] = data

    def _pop_from_front_stack(self):
        '''Removes the top value from the front stack and returns it'''
        if self.head_1 is None:
            raise Exception("stack 1 is empty")

        value = self.stack[self.head_1]
        self.stack[self.head_1] = None

        if self.head_1 == 0:
            self.head_1 = None
        elif self.head_1 > 0:
            self.head_1 -= 1

        return value

    def _pop_from_back_stack(self):
        '''Removes the top value from the back stack and returns it'''
        if self.head_2 is None:
            raise Exception("Stack 2 is empty")

        value = self.stack[self.head_2]
        self.stack[self.head_2] = None

        if self.head_2 == len(self.stack) - 1:
            self.head_2 = None
        elif self.head_2 < len(self.stack) - 1:
            self.head_2 += 1

        return value

if __name__ == "__main__":
    my_stack = ArrayOfStacks(3)
    my_stack.push(4, 2)
    my_stack.push(2, 1)
    my_stack.push(1, 2)
    my_stack.push(7, 1)
    my_stack.push(100, 1)
