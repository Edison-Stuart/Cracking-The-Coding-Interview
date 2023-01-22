'''Make a function that returns the
   kth to last element of a singly linked list'''

'''
First we define the function which will accept
the head node of a linked list, and the index (k)
of element to be found

function(node, k):

then iterate through the list and find out how many total
items there are

	items_in_list = 1
	current_node = node
	while current_node.next_node is not None:
		items_in_list += 1
		current_node = current_node.next_node

if k > items_in_list you would return with a negative case
(perhaps -1), indicating that there is no Kth to last element

	if k > items_in_list:
		return -1

if k = items_in_list then the Kth to last element would be
the head node, so we return index 0

	if k = items_in_list:
		return 0

finally, we just take the value of items_in_list - (k + 1),
which would be the index of the item we are looking for

	return items_in_list - (k + 1)
'''

def kth_to_last(node, k):
    items_in_list = 1
    current_node = node

    while current_node.next_node is not None:
        items_in_list += 1
        current_node = current_node.next_node
	
    if k > items_in_list:
        return -1
	
    if k == items_in_list:
        return 0
	
    return items_in_list - (k + 1)
