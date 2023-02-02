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

We will call this modified class ArrayOfStacks

	}

Now in order to change this ArrayOfStacks class to work with
three stacks we have to add a stack in the middle of the array.
To do this we have to keep track of
1) the head of the stack and
2) the tail of the stack.
We have to do this because our front stack and back stack have tails
at the start of the aray and the end of the array respectively, but
the middle stack does not have this built in end.

We will also rename head_1 and head_2 to head_front and head_back
as for now, we will not store the head pointers in an array, and accept a variable
array size that will determine the size of the array which our stacks will be housed in.

    constructor(array_size) {
    		self.stack = [null] * array_size
    		self.head_back = len(self.stack) - 1
            self.head_front = 0
            self.middle[floor(array_size / 2), floor(array_size / 2)] // head, tail
    	}

We can allocate space for our stacks dynamically
by shifting the middle stack over when there is an
overlap about to happen.

The code for pushing to the front or back stack will
now have to include a check to make sure there is space
for the stack to grow.

    _push_to_front_stack(self, data) {

We now need to ensure there is space for the
front stack to begin. There is the case that the
middle and back stack have grown such that the front
stack wil have no space.
We do this by checking if the middle's tail
pointer is the same as the front's head pointer.
If it is the same, we raise an exception

        if (self.head_front == self.middle[1]) {
            raise Exception("No more space in array")
        }
        elif (self.head_front == 0 && self.stack[head_front] == null) {

If the head_front has space, and it is set to 0, along with
stack[head_front] being empty, we just push the data to that index.

            self.stack[self.head_front] = data

        }

Then we check if the head would overlap with the middle if added to, if so,
we also check if the middle would overlap with the back if moved, if so,
we then raise an execption because there is no more space left in the array

        elif (self.head_front + 1 == self.middle[1] && self.middle[0] + 1 == self.head_back) {
            raise Exception("No more space in array")
        }

If the above check does not return true, but the front stack will
still overlap, we will then shift the middle stack the opposite direction
the front stack is growing. We will write a new function to do this called
_shift_middle.

        elif (self.head_front + 1 == self.middle[1]) {
            self._shift_middle(1)

After we have made sure there is enough space, we can then
add 1 to the front head value, then use that index to put
our data into the array.

            self.head_front += 1
            self.stack[self.head_front] = data
        }
        else {

Otherwise, if no shifting was needed, we can just add one to the index
and put the data where it belongs.

            self.head_front += 1
            self.stack[self.head_front] = data
        }

    }

We have to make similar changes to _push_to_back_stack.

    def _push_to_back_stack(self, data) {


We start by doing the same check on the head


        if (self.head_back == self.middle[0]) {
            raise Exception("No more space in array")
        }
        elif (self.head_back == len(self.stack) - 1 && self.stack[self.head_back] == null) {
            self.stack[self.head_back] = data
        }

We do the same check for space in the opposite direction

        elif (self.head_back -1 == self.middle[1] && self.middle[0] - 1 == self.head_front) {
            raise Exception("No more space in array")
        }

Then if there is no exception, we again check for collisions,
and move the middle if needed along with decreasing the index
and adding the data.

        elif (self.head_back - 1 == self.middle[1]) {
            self._shift_middle(-1)
            self.head_back -= 1
            self.stack[self.head_back] = data
        }

After these checks have passed and space is available,
we add to the stack like before.
        else {
        self.head_back -= 1
        self.stack[self.head_back] = data
        }
    }

Now that we have made these changes to pushing from both sides,
lets implement a function that will simply shift the middle stack.
We could make it so the stack is put in between the open space that is left
in order to decrease the amount of times this operation needs to run.
For now we will just move the middle stack by 1.


    _shift_middle(self, direction) {

First we should check which direction we are shifting

        if (direction < 0) {

if the direction is negative, we shift left.
We shift left by looping through the range from the tail
node, middle[0], and the head node, middle[1] + 1

            for (i in range(self.middle[0], self.middle[1] + 1)) {
            self.stack[i + direction] = self.stack[i]
        }

After that, we want to shift the head and tail pointer back 1 as well.

            self.middle[0] -= 1
            self.middle[1] -= 1
        }

        elif (direction > 0) {

if the direction is positive, we shift right.
We shift right by again, looping through the range; but this time
reversed.

            reversed_range = reversed(range(self.middle[0], self.middle[1] + 1))

with the reversed range, we can do the same translation as before

            for (i in reversed_range) {
            self.stack[i + direction] = self.stack[i]
            }

After we loop, we then increase the pointer value for the
middle head and tail.

            self.middle[0] += 1
            self.middle[1] += 1
        }
    }


With the hard part out of the way, now we just have to implement
the _push_to_middle function, and then the pop function.


for pushing to the middle stack, we will first check the middle has not been pushed
into. we will then check if the middle is empty.
If not, we then do a similar check to the last functions for head collisions,
moving the middle stack if needed.

    _push_to_middle(self, data) {
        if (self.middle[1] == self.head_back) {
            raise Exception("No more space in array")
        }
        elif (self.middle[0] == self.middle[1] && self.stack[self.middle[0]] == null) {
            self.stack[self.middle[0]] = data
        }
        elif (self.middle[1] + 1 == self.head_back && self.middle[0] - 1 == self.head_front) {
            raise Exception("No more space in array")
        }
        elif (self.middle[1] + 1 == self.head_back) {
            _shift_middle(-1)
            self.middle[1] += 1
            self.stack[self.middle] = data
        }

After those checks pass, we know there is enough space so we
add one to the middle head index and put our data there.

        else {
            self.middle[1] += 1
            self.stack[self.middle] = data
        }


We now have to remake _pop_from_front_stack and _pop_from_back_stack,
along with creating _pop_from_middle_stack.

let's start with pop from front stack

    _pop_from_front_stack(self) {

We first check if there are any values in the stack

        if (self.head_front == 0 && self.stack[self.head_front] == null) {
            raise Exception("No more space in array")
        }
        elif (self.head_front == 0) {

If the head_front is 0 but there is data in the array,
we save that data to a variable to be returned then set
the stack position to null.

            value = self.stack[self.head_front]
            self.stack[self.head_front] = null
        }
        else {

If there is data in the stack, and the head front is not 0,
we want to do the same thing as before, but this time we
also decrease the head_front value by 1.

            value = self.stack[self.head_front]
            self.stack[self.head_front] = null
            self.head_front -= 1
        }

at the end we return the value

        return value

    }


Now for the _pop_from_back_stack function

    _pop_from_back_stack(self) {
        if (self.head_back == len(self.stack) - 1 && self.stack[self.head_back] == null) {
            raise Exception("No more space in array")
        }
        elif (self.head_back == len(self.stack) - 1) {
            value = self.stack[self.head_back]
            self.stack[self.head_back] = null
        }
        else {
            value = self.stack[self.head_back]
            self.stack[self.head_back = null]
            self.head_back += 1
        }
        retrn value
    }

The pop from back stack method is almost the same as the
pop from front stack method, just reversed.

Now for the _pop_from_middle_stack function


    _pop_from_middle_stack(self) {

We want to check that the middle head is not the same as tail,
as well as the stack at index middle_head is not empty

    if (self.middle[1] == self.middle[0] && self.stack[self.middle[1]] == null) {
            raise Exception("No more space in array")
    }
    elif (self.middle[1] == self.middle[0]) {
        value = self.stack[self.middle[1]]
        self.stack[self.middle[1]] = null
    }
    else {
        value = self.stack[self.middle[1]]
        self.stack[self.middle[1]] = null
        self.middle[1] -= 1
    }

We can also add the peek method

    peek(self, stack) {
        if (stack == 0) {
            value = self.stack[self.head_front]
        }
        elif (stack == 1) {
            value = self.stack[self.middle[1]]
        }
        elif (stack == 2) {
            value = self.stack[self.head_back]
        }
        return value
    }

This stack class has all the method needed except is_empty, which
can be added later.

'''
# class ArrayOfStacks:
#     '''A class that uses an array which stores a stack in a subset of the array'''
#     def __init__(self, stack_size):
#         '''Accepts size limit of stack, no greater than 9'''
#         self.stack = [None] * 20
#         self.head_1 = None
#         self.head_2 = None
#         self.stack_size = stack_size

#     def push(self, data, stack):
#         '''Accepts data and then which stack, 1 or 2, to
# 		   push the data to'''
#         if stack == 1:
#             self._push_to_front_stack(data)
#         elif stack == 2:
#             self._push_to_back_stack(data)
#         else:
#             raise Exception("value 'stack' should be 1 or 2")

#     def pop(self, stack):
#         '''Accepts a stack number, 1 or 2, and pops out
# 		   the top value from that stack'''
#         value = None
#         if stack == 1:
#             value = self._pop_from_front_stack()
#         elif stack == 2:
#             value = self._pop_from_back_stack()
#         else:
#             raise Exception("value 'stack' should be 1 or 2")
#         return value

#     def peek(self, stack):
#         '''Method accepts 1 or 2, denoting which stack
# 		   you want to access. Then returns the top value
# 		   from that stack'''
#         value = None
#         if stack == 1:
#             value = self.stack[self.head_1]
#         elif stack == 2:
#             value = self.stack[self.head_2]
#         return value

#     def _push_to_front_stack(self, data):
#         '''Takes data and puts it into stack 1'''
#         if self.head_1 is None:
#             self.head_1 = 0
#             self.stack[self.head_1] = data
#         else:
#             if self.head_1 + 1 == self.stack_size:
#                 raise Exception("stack 1 at capacity")
#             self.head_1 += 1
#             self.stack[self.head_1] = data

#     def _push_to_back_stack(self, data):
#         '''Takes data and puts it into stack 2'''
#         if self.head_2 is None:
#             self.head_2 = len(self.stack) - 1
#             self.stack[self.head_2] = data
#         else:
#             if (len(self.stack) - self.head_2) == self.stack_size:
#                 raise Exception("stack 2 is at capacity")
#             self.head_2 -= 1
#             self.stack[self.head_2] = data

#     def _pop_from_front_stack(self):
#         '''Removes the top value from the front stack and returns it'''
#         if self.head_1 is None:
#             raise Exception("stack 1 is empty")

#         value = self.stack[self.head_1]
#         self.stack[self.head_1] = None

#         if self.head_1 == 0:
#             self.head_1 = None
#         elif self.head_1 > 0:
#             self.head_1 -= 1

#         return value

#     def _pop_from_back_stack(self):
#         '''Removes the top value from the back stack and returns it'''
#         if self.head_2 is None:
#             raise Exception("Stack 2 is empty")

#         value = self.stack[self.head_2]
#         self.stack[self.head_2] = None

#         if self.head_2 == len(self.stack) - 1:
#             self.head_2 = None
#         elif self.head_2 < len(self.stack) - 1:
#             self.head_2 += 1

#         return value

import math

class ArrayOfStacks:

    def __init__(self, array_size):
        self.stack = [None] * array_size
        self.head_back = len(self.stack) - 1
        self.head_front = 0
        self.middle = [math.floor(array_size / 2), math.floor(array_size / 2)] # head, tail


    def push(self, data, stack):
        '''Accepts data and then which stack, 1 or 2, to
		   push the data to'''
        if stack == 1:
            self._push_to_front_stack(data)
        elif stack == 2:
            self._push_to_middle_stack(data)
        elif stack == 3:
            self._push_to_back_stack(data)
        else:
            raise Exception("value 'stack' should be 1, 2, or 3")

    def pop(self, stack):
        '''Accepts a stack number, 1, 2, or 3, and pops out
		   the top value from that stack'''
        value = None
        if stack == 1:
            value = self._pop_from_front_stack()
        elif stack == 2:
            value = self._pop_from_middle_stack()
        elif stack == 3:
            value = self._pop_from_back_stack()
        else:
            raise Exception("value 'stack' should be 1, 2, or 3")
        return value

    def _push_to_front_stack(self, data):
        if self.head_front == self.middle[1]:
            raise MemoryError("No more space in array")

        if self.head_front == 0 and self.stack[self.head_front] is None:
            self.stack[self.head_front] = data

        elif self.head_front + 1 == self.middle[0] and self.middle[1] + 1 == self.head_back:
            raise MemoryError("No more space in array")

        elif self.head_front + 1 == self.middle[1]:
            self._shift_middle(1)
            self.head_front += 1
            self.stack[self.head_front] = data

        else:
            self.head_front += 1
            self.stack[self.head_front] = data

    def _push_to_back_stack(self, data):
        if self.head_back == self.middle[0]:
            raise MemoryError("No more space in array")

        elif self.head_back == len(self.stack) - 1 and self.stack[self.head_back] is None:
            self.stack[self.head_back] = data

        elif self.head_back -1 == self.middle[1] and self.middle[0] - 1 == self.head_front:
            raise MemoryError("No more space in array")

        elif self.head_back - 1 == self.middle[1]:
            self._shift_middle(-1)
            self.head_back -= 1
            self.stack[self.head_back] = data

        else:
            self.head_back -= 1
            self.stack[self.head_back] = data

    def _push_to_middle_stack(self, data):
        if self.middle[1] == self.head_back:
            raise MemoryError("No more space in array")

        if self.middle[0] == self.middle[1] and self.stack[self.middle[0]] is None:
            self.stack[self.middle[0]] = data

        elif self.middle[1] + 1 == self.head_back and self.middle[0] - 1 == self.head_front:
            raise MemoryError("No more space in array")

        elif self.middle[1] + 1 == self.head_back:
            self._shift_middle(-1)
            self.middle[1] += 1
            self.stack[self.middle[1]] = data

        else:
            self.middle[1] += 1
            self.stack[self.middle[1]] = data

    def _shift_middle(self, direction):
        if direction < 0:
            for i in range(self.middle[0], self.middle[1] + 1):
                self.stack[i + direction] = self.stack[i]

            self.middle[0] -= 1
            self.middle[1] -= 1

        elif direction > 0:
            reversed_range = reversed(range(self.middle[0], self.middle[1] + 1))
            for i in reversed_range:
                self.stack[i + direction] = self.stack[i]

            self.middle[0] += 1
            self.middle[1] += 1

    def _pop_from_front_stack(self):
        if self.head_front == 0 and self.stack[self.head_front] is None:
            raise IndexError("No data in stack")

        if self.head_front == 0:
            value = self.stack[self.head_front]
            self.stack[self.head_front] = None

        else:
            value = self.stack[self.head_front]
            self.stack[self.head_front] = None
            self.head_front -= 1

        return value

    def _pop_from_back_stack(self):
        if self.head_back == len(self.stack) - 1 and self.stack[self.head_back] is None:
            raise IndexError("No data in stack")

        if self.head_back == len(self.stack) - 1:
            value = self.stack[self.head_back]
            self.stack[self.head_back] = None

        else:
            value = self.stack[self.head_back]
            self.stack[self.head_back] = None
            self.head_back += 1

        return value

    def _pop_from_middle_stack(self):
        if self.middle[1] == self.middle[0] and self.stack[self.middle[1]] is None:
            raise IndexError("No data in stack")

        elif self.middle[1] == self.middle[0]:
            value = self.stack[self.middle[1]]
            self.stack[self.middle[1]] = None

        else:
            value = self.stack[self.middle[1]]
            self.stack[self.middle[1]] = None
            self.middle[1] -= 1

        return value

    def peek(self, stack):
        if stack == 1:
            value = self.stack[self.head_front]
        elif stack == 2:
            value = self.stack[self.middle[1]]
        elif stack == 3:
            value = self.stack[self.head_back]
        elif stack not in [1, 2, 3]:
            raise Exception('can only peek into stack 1, 2, or 3')
        return value
