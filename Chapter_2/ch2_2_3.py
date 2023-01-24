'''Delete middle node from linked list
   with access to only the node to be deleted'''

'''
First we want to make sure that this node is not the last node

function(node):
    if node.next_node is none:
		return False

next we simply copy the contents of the next node to this node

    next_node = node.next_node
	node.data = next_node.data
	node.next = next_node.next_node

then we return True on a successful operation

    return True

And that's it, basically as I understand it currently we
are just moving the next node to the current node so the current
node is 'deleted' and there is no longer a reference to the
node we took from, just this new node
'''

def delete_middle(node):
    if node.next_node is None:
        return False
    next_node = node.next_node
    node.data = next_node.data
    node.next_node = next_node.next_node

    return True
