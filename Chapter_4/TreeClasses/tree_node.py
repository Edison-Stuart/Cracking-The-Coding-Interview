'''
This module holds the class TreeNode and is used
for building a tree data structure. The module also
holds the function build_tree which will create a
binary tree with the info passed into the function.
'''
from .tree_queue import Queue

class TreeNode:
    """This class creates a TreeNode that holds data and a list of children nodes."""

    def __init__(self, data: any):
        """
		Creates a node with the values data, and children

		Args:
			data: data that will be stored in the tree node
		"""
        self.data = data
        self.left = None
        self.right = None

def build_tree(data: list) -> TreeNode:
    """
	Function that takes a list of data and uses it to build a tree.

	Args:
		data: The list of data that will be turned into tree nodes

	Returns:
		TreeNode: Will return the head node of newly created tree.

	Raises:
		TypeError: If type of data passed in is not list
		Exception: If list passed in is empty
	"""
    if not isinstance(data, list):
        raise TypeError('Data type must be list')
    if not data:
        raise Exception("No data in list")

    head_node = TreeNode(data[0])
    current_node = head_node
    nodes_to_be_filled = Queue()
    total_nodes = 1
    cur_index = 1

    while total_nodes < len(data) or not nodes_to_be_filled.is_empty():
        if current_node.data is None:
            current_node.data = data[cur_index]
            cur_index += 1

        if current_node.left is None and current_node.right is None:
            if total_nodes == len(data):
                current_node = nodes_to_be_filled.dequeue()
            elif total_nodes + 2 <= len(data):
                current_node.left = TreeNode(None)
                current_node.right = TreeNode(None)
                total_nodes += 2
                nodes_to_be_filled.enqueue(current_node.left)
                nodes_to_be_filled.enqueue(current_node.right)
                current_node = nodes_to_be_filled.dequeue()
            else:
                current_node.left = TreeNode(None)
                total_nodes += 1
                nodes_to_be_filled.enqueue(current_node.left)
                current_node = nodes_to_be_filled.dequeue()

    if len(data) != 1:
        current_node.data = data[cur_index]

    return head_node
