# def depth_first_search_recursive(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         depth_first_search_recursive(graph, next, visited)
#     return visited

'''
Above is an implementation of a Depth first search. The function expects an adjacency list
and returns a set of all the visited nodes.

In order to implement a DFS using recursion, all you have to do is mark nodes that you have visited,
in this case the person who wrote this function is using a set of nodes that they are adding to,
After you mark the current node you are visiting,
you make recursive calls for each of the nodes neighbors.
Because of the way this function will run,
The path the algorithm takes will search as deep as it can go before searching any of the
top level neighbors.

We can break this DFS down into the basic elements.

def DFS(graph, start):

We don't neccecarily need this visited variable depending on the structure of our tree and
tree nodes. We can just use a marked instance variable on each of the nodes in order to keep
track of what has been marked.

We first will mark the node that we are visiting

	start.marked = True

Then we can simply search all of the neighbors of this node if they are not already marked.
We will assume that we are recieving an adjacency list that represents our graph.

	for next_node in graph[start]:
		if next_node.marked is not True:
			DFS(graph, next_node)

This function has nothing to return with how we have built it, in fact,
this function does not do anything during the search. Perhaps we could be searching
for a specific node or just simply printing out the contents of each node.
However we decide to use this algorithm, it does not neccecarily have to return anything.
It could just be making tranformations to our data or gathering a list of specific nodes that
have values we are looking for.
'''
