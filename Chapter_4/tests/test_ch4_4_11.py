from ..ch4_4_11 import BinarySearchTree, Node

def test_get_random_node():
    my_tree = BinarySearchTree([5,10,0,-10,35,2,50,41,9])
    random_node = my_tree.get_random_node()
    assert isinstance(random_node, Node)
    assert random_node.data in [5,10,0,-10,35,2,50,41,9]
