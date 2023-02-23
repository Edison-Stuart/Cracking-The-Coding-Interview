'''
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth. I.E tree wit ha depth of 3 has 3 linked lists

In order to do this we can use a depth function to keep track of the depth
that we are at. We can use a pre order traversal while passing our tree nodes,
as well as the depth we are at to each call of the function.

To get the depth of our tree at current position, we can
use a recursive function that will traverse to the bottom of the
tree and bubble up a depth value

	def get_tree_depth(head_node: TreeNode) -> int:
	    if head_node == None:
	        return 0
	    if head_node.left == None and head_node.right == None:
	        return 1
	    else:
	        depthLeft = 1 + depth(head_node.left)
	        depthRight = 1 + depth(head_node.right)
	        if depthLeft > depthRight:
	            return depthLeft
	        else:
	            return depthRight


In our convert tree depth to linked lists function, we can have the function accept
a node, a dictionary of lists, and a value for the depth that will default at none.

	def convert_tree_depth_to_linked_lists(head_node: TreeNode, linked_lists={}, depth=None):

if the depth is none, I.E our function has been called for the first time, we will set
our depth to the result of our get_tree_depth function.

	if depth is None:
        depth = get_tree_depth(head_node)

we can use our depth value for the dictionary key and store a linked list
head node or add to a linked list depending if that value is empty or not.

	if linked_lists.get(depth) is None:
		linked_lists[depth] = Node(head_node.data)
    else:
		linked_lists[depth].append_to_tail(head_node.data)

if the depth is equal to one, we will return our linked_lists

		if depth == 1:
			return linked_lists

Then we can do the rest of our pre order traversal.

We check to make sure that the left node is not None,
then we set our linked_lists equal to the result
of calling ourselves with the left node, the linked_lists,
and the depth minus one as to check the previous level.

We do the same check with the right node, then at the end we return our linked_lists.

	if head_node.left is not None:
		linked_lists = convert_tree_depth_to_linked_lists(head_node.left, linked_lists, depth - 1)
    if head_node.right is not None:
		linked_lists = convert_tree_depth_to_linked_lists(head_node.right, linked_lists, depth - 1)

    return linked_lists
'''
from .linked_list.list_node import Node
from .TreeClasses.tree_node import TreeNode

def get_tree_depth(head_node: TreeNode) -> int:
    '''
    Returns the depth of a linked list

    Args:
        head_node: The tree node that will be searched
            to determine the max depth of the tree.

    returns:
        depth: An int value that represents the depth of the tree.
    '''
    if head_node is None:
        return 0
    if head_node.left is None and head_node.right is None:
        return 1

    depth_left = 1 + get_tree_depth(head_node.left)
    depth_right = 1 + get_tree_depth(head_node.right)
    if depth_left > depth_right:
        return depth_left
    return depth_right


def tree_to_linked_lists(head_node: TreeNode, linked_lists: list = None, depth: int = None) -> dict:
    '''
    Converts a tree to a dict of linked lists.

    Args:
        head_node: The head node that will be used to search tree.

        linked_lists: A dictionary of linked lists used to
            keep track of all the lists at a key of level depth.

        depth: The depth of the tree, is calculated when function is called.

    Raises:
        Exception: If Linked listis null with non null depth

    Returns:
        linked_lists: The complete dictionary of linked lists for each level
            of the tree.
    '''
    if depth is None:
        depth = 0
        linked_lists = [None] * get_tree_depth(head_node)
    elif linked_lists is None:
        raise Exception("Linked list is null with non-null depth")

    if linked_lists[depth] is None:
        linked_lists[depth] = Node(head_node.data)
    else:
        linked_lists[depth].append_to_tail(head_node.data)

    if depth < len(linked_lists) - 1:
        if head_node.left is not None:
            linked_lists = tree_to_linked_lists(head_node.left, linked_lists, depth + 1)
        if head_node.right is not None:
            linked_lists = tree_to_linked_lists(head_node.right, linked_lists, depth + 1)
    return linked_lists
