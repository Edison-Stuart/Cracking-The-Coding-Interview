'''
Given a directed graph and two nodes, S and E, design an algorithm to
find out whether there is a route from S to E.

There are multiple ways to go about this, the way I have chosen
was to preform a depth first search using a class and recursion.

Our class will accept an adjacency list of type dict, and will use this dictionary
to create a list of keys which we will call vertices.

    class CheckForPath {
        constructor(this, adjacency_list) {
        this.adjacency_list = adjacency_list
        this.vertices = adjacency_list.keys()
        }

We can then make our function that actually checks if there is an available path.
This function will be called are_nodes_connected, and will accept a source, or start;
and a target, or end. The function will also have two keyword arguments, visited and target_path.
These two kwargs will help us keep track of local state through recursive function calls.

        are_nodes_connected(this, source, target, visited=None, target_path=None) {

We start my making a path out variable and constructing visited and target_path if None.

            path_out = None
            if visited is None:
                local_visited = {}
                for vertex in this.vertices:
                    local_visited[vertex] = False
            else:

If visited is not none, then we simple make a copy of it and save that to local_visited.

                local_visited = deepcopy(visited)
            
We do the same with target_path

            if target_path is None:
                local_path = []
            else:
                local_path = deepcopy(target_path)


We then mark our current node visited and append the node to our local_path

        local_visited[source] = True
        local_path.append(source)


We can check if our source is our target, and if it is we set path_out to local_path;
because that local path will be the path to our target.

        if source == target:
            path_out = local_path

If source is not target, we then make sure we can continue searching the adjacent nodes by making
a check to see that there are adjacent nodes.

If there are adjacent nodes, we loop through them and if they have not been visited,
we set path_out to the result of a recursive function call.

        elif self.adjacency_list[source] is not None:
            for i in self.adjacency_list[source]:
                if local_visited[i] is False:
                    path_out = self.are_nodes_connected(i, target, local_visited, local_path)

At the end of the recursion our path_out will be set to the first path the algorithm has found,
Note that this may not be the shortest path. We are simply checking if there is a path at all.
If there is a path, we get the path back as a list; if there is no path, we get back a None value.

        return path_out
}
'''
from copy import deepcopy

class GraphCycleException(Exception):
    def __init__(self, message="Cycle in graph is not allowed"):
        self.message = message
        super().__init__(self.message)

class CheckForPath:
    '''
    Args:
        adjacency_list(dict): A dictionary of nodes and what they are adjacent to.
    '''
    def __init__(self, adjacency_list: dict):
        self.adjacency_list = adjacency_list
        self.vertices = adjacency_list.keys()

    def are_nodes_connected(self, source, target, visited=None, target_path=None) -> list or None:
        """
        Obtains list of all paths from source to target, via DFS

        Args:
            source(any): The starting node we will be searching from in our graph
            target(any): The ending node we will be searching to in our graph
            visited(None / dict): A dictionary where vertices of the graph
                are keys and values are a boolean representing if the node
                has been searched or not.
            target_path(None / list): A list of nodes that have been searched in order
                to reach the target node.

        Returns:
            path_out(None / list): has the value of None if target path does not exist,
                otherwise has the value of a list of the nodes traversed.

        Raises:
            GraphCycleException: If the search finds any cycles that intersect
            Exception: If during the search another unexpected exception is thrown.

        """
        try:
            path_out = None
            if visited is None:
                local_visited = {}
                for vertex in self.vertices:
                    local_visited[vertex] = False
            else:
                local_visited = deepcopy(visited)

            if target_path is None:
                local_path = []
            else:
                local_path = deepcopy(target_path)

            if set(local_path).intersection(set(self.adjacency_list[source])):
                raise GraphCycleException(
                    'Cycle present in path; ' +
                    'source %s neighbors %s intersect path %s' %
                    (source, self.adjacency_list[source], local_path)
                )

            local_visited[source] = True
            local_path.append(source)

            if source == target:
                path_out = local_path
            elif self.adjacency_list[source] is not None:
                for i in self.adjacency_list[source]:
                    if local_visited[i] is False:
                        path_out = self.are_nodes_connected(i, target, local_visited, local_path)
            return path_out
        except Exception as error:
            raise Exception('While obtaining paths: %s' % error)
