'''
First Common Ancestor: Design an algorithm and write code
to find the first common ancestor of two nodes in a binary tree.
Avoid storing nodes in an additional data structure.

NOTE: This is not necessarily a binary search tree

We can do this by thinking of this binary tree as a non directed
graph. This graph will have consist of a series of vertices and edges.

our function, find_first_common_ancestor, will accept two parameters.
these two parameters will be our target1 and target2.

    function find_first_common_ancestor(target1: GraphNode, target2: GraphNode) -> GraphNode:


We can use these nodes to create pointers and traverse the tree upwards,
marking the edges that we pass. We also create the first_common_ancestor
variable which will be set to None


        pointer1 = target1
        pointer2 = target2
        first_common_ancestor = None


For pointer1 we will use a while loop to traverse up to the root of the tree,
which in this case has its edges[0] (previous edge) set to None as it is the root,
while marking each edge as we traverse with the value 'pointer1'


        while (pointer1.edges[0] !== None):
            pointer1.edges[0].marked_by.append('pointer1')
            pointer1 = pointer1.edges[0].vertices[0]


After we traverse the tree and mark the edges we will do another while loop
going up to the root of the tree with the second pointer.
We in this second loop can look for the pointer1 marking in edge[0].marked_by,
if we find it then we can stop the loop and assume the current target of the
pointer is our first common ancestor.


        while (pointer2.edges[0] !== None):
            if (pointer2.edges[0].marked_by and 'pointer1' in pointer2.edges[0].marked_by):
                first_common_ancestor = pointer2
                break
            pointer2 = pointer2.edges[0].vertices[0]


If the second pointer reaches the top
without breaking, then we know that the 'root' node will be our first common ancestor;
so we just set our pointer2, which is already the root node, to the first_common_ancestor

        if (first_common_ancestor === None):
            first_common_ancestor = pointer2

We then also have to check if our first common ancestor is equal to either of
the targets, this could be the case if one target is a child of another target.
If this is the case we simply set first_common_ancestor to the node previous, or
first_common_ancestor.edges[0].vertices[0].

        if (first_common_ancestor in (target1, target2)):
            first_common_ancestor = first_common_ancestor.edges[0].vertices[0]

We then return the first_common_ancestor

        return first_common_ancestor
'''
from .GraphClasses.graph import GraphNode

def find_first_common_ancestor(target1: GraphNode, target2: GraphNode) -> GraphNode:
    '''
    Given two target nodes in a binary tree, will return the first common ancestor between them

    Args:
        target1, target2: The two nodes that will be used in the search for the common ancestor.

    Returns:
        first_common_ancestor: The closest node to both targets that has both target as
            child nodes.

    Raises:
        Exeption: When either target node passed in is the root node of the tree
    '''
    pointer1 = target1
    pointer2 = target2
    first_common_ancestor = None

    if pointer1.edges[0] is None or pointer2.edges[0] is None:
        raise Exception("Target node cannot be the root node of a tree")

    while pointer1.edges[0] is not None:
        pointer1.edges[0].marked_by.append('pointer1')
        pointer1 = pointer1.edges[0].vertices[0]

    while pointer2.edges[0] is not None:
        if pointer2.edges[0].marked_by and 'pointer1' in pointer2.edges[0].marked_by:
            first_common_ancestor = pointer2
            break
        pointer2 = pointer2.edges[0].vertices[0]

    if first_common_ancestor is None:
        first_common_ancestor = pointer2
    if first_common_ancestor in (target1, target2):
        first_common_ancestor = first_common_ancestor.edges[0].vertices[0]
    return first_common_ancestor
