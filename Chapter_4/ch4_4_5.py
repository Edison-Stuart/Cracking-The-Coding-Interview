'''
Write a function to determine if a tree is
   a binary search tree or not.


A BST is a tree where all the nodes are arranged as such

n being the current node:

	all left descendents <= n < all right descendents

For this we can preform an in order search through the tree,
adding each node to a stack. When we are finished with that
we can simply unstack the data and check that it is in order.

we can make our "visit" function push the item on our stack, which we can pass to it and
get returned back.

lets start by defining our validate_bst function

	def validate_BST(head_node: TreeNode, my_stack: Stack = None) -> Bool:
        if my_stack is None:
            my_stack = Stack()
		if head_node:
			validate_BST(head_node.left, my_stack)
			my_stack = visit(head_node, my_stack)
			validate_BST(head_node.right, my_stack)

and for the visit function we simply do this

    def visit(node: TreeNode, stack: Stack):
        stack.push(node)
        return stack


Now, for checking if the data is valid, we have to first unstack it,
then go through it and make sure that every value is bigger than the last.

For this we can actually put the in order search into a different function which returns a stack,
then with the data we get back we just have to unstack and check it.


So, we take the function that we made and rename it to something like
collect_tree_data_in_order

    def collect_tree_data_in_order(node: TreeNode, my_stack: Stack = None) -> Bool:
        if my_stack is None:
            my_stack = Stack()
		if node:
			collect_tree_data_in_order(node.left, my_stack)
			my_stack = visit(node, my_stack)
			collect_tree_data_in_order(node.right, my_stack)
        return my_stack

Then from that we return the stack.

our Validate_BST function will then be unstacking and checking the data

def validate_BST(head_node: TreeNode) -> bool:
    stack_of_nodes = collect_tree_data_in_order(head_node)
    list_of_data = []

Unstacking the data

    while stack_of_nodes.is_empty() is False:
        list_of_data.push(stack_of_nodes.pop())

for checking the data for validity, we can loop through our list of data reversed
and check that data[i] > data[i + 1]. if this ever is true, we return false.
Otherwise we return true

    for i, item in enumerate(list_of_data):
        if item < list_of_data[i + 1]:
            return False
    return True

we can also break the unstacking into a seperate function which
returns a list to us



'''
from symbol import return_stmt
from TreeClasses.tree_node import build_tree, TreeNode
from TreeClasses.tree_stack import Stack

def visit(node: TreeNode, stack: Stack) -> Stack:
    stack.push(node)
    return stack

def collect_tree_data_in_order(head_node: TreeNode, my_stack: Stack = None) -> Stack:
    if my_stack is None:
        my_stack = Stack()
        head_node.data = (head_node.data, True)
    elif head_node:
        head_node.data = (head_node.data, False)
    if head_node:
        collect_tree_data_in_order(head_node.left, my_stack)
        my_stack = visit(head_node, my_stack)
        collect_tree_data_in_order(head_node.right, my_stack)
    return my_stack

def unstack_data(stack: Stack) -> list:
    return_list = []
    while stack.is_empty() is False:
        return_list.append(stack.pop().data)
    return return_list

def validate_BST(head_node: TreeNode) -> bool:
    stack_of_nodes = collect_tree_data_in_order(head_node)
    list_of_data = unstack_data(stack_of_nodes)
    head_node_found = False
    list_of_data.reverse()

    for i, item in enumerate(list_of_data):
        if i == len(list_of_data) - 1:
            break
        if item[1] is True:
            head_node_found = True
        if head_node_found is False:
            if item[0] > list_of_data[i + 1][0]:
                return False
        else:
            if item[0] >= list_of_data[i + 1][0]:
                return False
    return True

if __name__ == "__main__":
    my_list = [10,8,12,7,9,11,13,7, 7]
    my_tree = build_tree(my_list)
    print(validate_BST(my_tree))
