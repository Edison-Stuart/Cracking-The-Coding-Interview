from ..TreeClasses.tree_node import build_tree
from ..ch4_4_5 import validate_bst

VALID_TEST_DATA = [
	[2,1,3],
	[0],
	[0,-1],
	[32,26,47,19,None,None,56,None,25],
	[120,70,140,50,100,130,160,20,55,75,110,125,135,150,200],
	]

INVALID_TEST_DATA = [
	[5,1,4,None,None,3,6],
	[1,1],
	[5,14,None,1],
	[5,4,6,None,None,3,7],
	[10,5,15,None,None,6,20],
	[32,26,47,19,None,None,56,None,27],
	[3,None,30,10,None,None,15,None,45],
	[120,70,140,50,100,130,160,20,55,75,110,119,135,150,200],
	]

def test_validate_bst_true():
    for test_case in VALID_TEST_DATA:
        head_node = build_tree(test_case)
        assert validate_bst(head_node) is True

def test_validate_bst_false():
    for test_case in INVALID_TEST_DATA:
        head_node = build_tree(test_case)
        assert validate_bst(head_node) is False
