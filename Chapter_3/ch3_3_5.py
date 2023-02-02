'''Create a program that sorts a stack such that
   the smallest items are on top. You may use a temporary
   stack but no additional data structures.'''

'''
First we want to create a function that accepts the a stack

	def sort_stack_small_on_top(stack):

Then we want to first, make a variable for the temp stack,
make a variable for the temp value, and make a variable
for the current_node

    sorted_stack = Stack()
	unsorted_stack = stack
	temp_val = None

if the sorted_stack is empty,
we want to push the top item from our unsorted_stack to our sorted_stack

    while unsorted_stack.is_empty() is False:
    		if sorted_stack.is_empty():
    			sorted_stack.push(unsorted_stack.pop())


if the sorted_stack is not empty,
then we save our popped value as the temp_val, and put values that are higher
than the temp value from sorted_stack into unsorted_stack then temp is pushed into
the sorted stack and we do the process again.

		else:
			temp_val = unsorted_stack.pop()
			while sorted_stack.peek() > temp_val:
				unsorted_stack.push(sorted_stack.pop())
			sorted_stack.push(temp_val)

After this, we simply copy the elements back from sorted_stack into unsorted_stack

    while sorted_stack.is_empty() is False:
		unsorted_stack.push(sorted_stack.pop)

'''


from data_structures.stack import Stack

def sort_stack_small_on_top(unsorted_stack):
    sorted_stack = Stack()
    while unsorted_stack.is_empty() is False:
        temp_val = unsorted_stack.pop()
        while sorted_stack.is_empty() is False and sorted_stack.peek() > temp_val:
            unsorted_stack.push(sorted_stack.pop())
        sorted_stack.push(temp_val)

    while True:
        if sorted_stack.is_empty():
            break
        unsorted_stack.push(sorted_stack.pop())
