'''
Implement a Binary Search Tree class from scratch that has the insert, find, delete,
and getRandomNode methods. getRandomNode should return a random node and have an equally likely
chance to return any given node.

There are multiple things that we can do to implement this. The solution that I
am going to use involves doing an in order traversal of the tree and saving each node
into an array. We will then generate a random number between 0 and len(array) - 1

All we do after that is return array[randint(0, len(array) - 1)]

we can generate a list of all our nodes with a helper function,
we can call this function _create_in_order_array.

This function will accept a list that is set to None by default,
this way we can build the list and return it.
It will also accept the parameter current_node which will also
be set to None by default. This way we can use recursion to create our list.

def _create_in_order_array(self, nodes=None, current_node=None):

We can check if this is the first call of the function if nodes as well
as current_node are set to None. If so, we make nodes a list and set
current_node to self.head.

    if nodes is None and current_node is None:
        nodes = []
        current_node = self.head

If this is not the first call, IE nodes is not None, but current_node is none,
that means we are at the bottom and can return nodes back as is.

    elif current_node is None:
        return

If we have both nodes and current_node, we can use recursive function call with
the left child of the current node.
This will go down the path all the way until we reach the end, at which point
we append the current node to nodes. We do the same on the right after we
append our current node, and in the end we return the whole nodes array.

NOTE: This array does not need to be made with an in order traversal, because we are
selecting a node at random the order of the nodes is not important.

    self._create_in_order_array(nodes, current_node.left)
    nodes.append(current_node)
    self._create_in_order_array(nodes, current_node.right)

    return nodes

So, to get started we can define our function
This function will take no arguments other than self.

    def get_random_node(self):

We will first generate our list of all nodes and set that value equal to the variable
node_list

    node_list = self._create_in_order_array()

We can then take the length of this array and create a random int between 0 and this length.

    random_index = randint(0, len(node_list) - 1)

We then just return the value node_list at index random_index.

    return node_list[random_index]

'''
from copy import deepcopy
import random

class Node:
    def __init__(self, data):
        '''
        A class that implements a node for a tree

        Args:
            data(any): The value that will be put in the nodes
                self.data instance variable.
        '''
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        '''Dunder method for Node class that gets the data out
            of a node when it is converted to a string

        Returns:
            str(self.data)
        '''
        return str(self.data)

def make_bst_from_sorted_array(arr: list) -> Node:
    '''
    A function that creates a BST from a sorted array

    Args:
        arr: The array of values that will be recursively
            converted to nodes in a tree.

    Returns:
        head_node: The head node of a bst
    '''
    if not arr:
        return None

    mid = (len(arr)) // 2

    node = Node(arr[mid])

    node.left = make_bst_from_sorted_array(arr[:mid])

    node.right = make_bst_from_sorted_array(arr[mid+1:])

    return node

class BinarySearchTree:
    def __init__(self, data: list = None) -> None:
        '''
        A class that creates a binary search tree with optional data passed in
        This tree will only hold int or float values

        Args:
			data: An optional list of data that the BST will be populated with
        '''
        self.head = None
        if not data:
            pass
        else:
            sorted_data = sorted(deepcopy(data))
            self.head = make_bst_from_sorted_array(sorted_data)

    def insert(self, data: int) -> None:
        '''
        Inserts data into the BST as a Node

        Args:
            data: The data that will be put into the tree.
        '''
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        prev_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data > data:
                prev_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                prev_node = current_node
                current_node = current_node.right
        if prev_node.data > data:
            prev_node.left = node
        else: prev_node.right = node

    def search(self, target: int) -> Node:
        '''
        A method that searches the BST for a specific target value.

        Args:
            target: The target value (an int or float) that will be searched
                for in the BST

        Returns:
            None: If the target was not found in the tree
            Node: The node containing the target data if it was found.
        '''
        current_node = self.head
        return_target = None

        while current_node is not None:
            if current_node.data == target:
                return_target = current_node
                break
            if current_node.data > target:
                current_node = current_node.left
            elif current_node.data < target:
                current_node = current_node.right
        return return_target

    def delete(self,root: Node, key: int) -> None:
        '''
        Method that removes a specific node given a key from the tree.

        Args:
            root: The root node of the tree we want to delete from
            key: An int value that is the key to one of our nodes in the tree.
                NOTE: this implementation will remove the first node with the value key
                that it finds.
        '''

        parent = None

        curr = root

        while curr and curr.data != key:
            parent = curr
            if key < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return root

        if curr.left is None and curr.right is None:

            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None

            else:
                root = None

        elif curr.left and curr.right:
            successor = self._get_min_key(curr.right)

            val = successor.data

            self.delete(root, successor.data)

            curr.data = val

        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right


            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child
        return root

    def get_random_node(self) -> Node:
        '''
        Gets a random node from the tree and returns it

        Returns: node: A random node selected from our tree.
        '''
        node_list = self._create_in_order_array()
        random_index = random.randint(0, len(node_list) - 1)
        return node_list[random_index]

    def _get_min_key(self, node: Node) -> Node:
        '''
        Accepts a root node of a subtree and returns the lowest node
        in the subtree.

        Args:
            node: The starting point for the traversal to the lowest value node.

        Returns:
            current: The lowest value node in the subtree
        '''
        current = node
        while current.left:
            current = current.left
        return current

    def _create_in_order_array(self, nodes: list=None, current_node: Node=None) -> list:
        '''
        Takes no arguments from user and generates a list of all nodes in tree.

        Args:
            nodes: A list of nodes to be passed through recursive function calls
                and built
            current_node: The node that will be appended to the array at the level
                this function is being called, as well as the node used to traverse to
                next nodes.

        Returns:
            nodes: The list of nodes build through recursive calls of this function.
        '''
        if nodes is None and current_node is None:
            nodes = []
            current_node = self.head
        elif current_node is None:
            return nodes

        self._create_in_order_array(nodes, current_node.left)
        nodes.append(current_node)
        self._create_in_order_array(nodes, current_node.right)

        return nodes
