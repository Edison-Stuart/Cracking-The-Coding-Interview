'''Implement a function to see if a linked list is
   a palindrome'''

'''
First we want to see if the list is of odd or even length

one way to do this is to iterate through
the list and find out how many total
items there are

we could also push every item in the list to an
array and check the length of that afterwards

function(node):
	my_arr = []
	current_node = node
	while current_node.next_node is not None:
		my_arr.append(node.data)
		current_node = current_node.next_node

then we check if the list is even or odd

    if len(my_arr) % 2 == 0

if the linked list is even we can just take two slices
of the list, first half and second half,
reverse one of them and compare them.

    first_half = my_arr[:(len(my_arr)/2)-1]
	second_half = my_arr[len(my_arr)/2:]
	

	if first_half == second_half.reverse():
		return True
	else:
		return False

if the linked list is odd, we take the middle item out of
the list and do the same thing.

    my_arr.delete((len(my_arr) / 2) -1)
'''

def linked_list_is_palindrome(node):
    my_arr = []
    current_node = node
    while current_node.next_node is not None:
        my_arr.append(current_node.data)
        current_node = current_node.next_node
    my_arr.append(current_node.data)

    if len(my_arr) % 2 == 0:
        first_half = my_arr[:(len(my_arr)/2)]
        second_half = my_arr[len(my_arr)/2:]
        second_half.reverse()
        return bool(first_half == second_half)

    my_arr.pop((len(my_arr) / 2))
    first_half = my_arr[:(len(my_arr)/2)]
    second_half = my_arr[len(my_arr)/2:]
    second_half.reverse()
    return bool(first_half == second_half)
