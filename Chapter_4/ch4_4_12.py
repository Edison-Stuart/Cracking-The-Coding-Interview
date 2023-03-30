'''
You are given a binary tree where each node contains an integer value (positive OR negative)
Design an algorithm to count the number of paths that sum to a given value. The path does not need
to start at the root or end at a leaf but it must only travel downwards.

For this problem we can first collect a list of all of the paths between all of the nodes.

We can make a class that will hold an adjacency list, as well as
an instance variable called 'paths'.

We can also collect the vertices by getting the keys from the adjacency list

    class CheckForPath:

        def __init__(self, adjacency_list: list):
            self.adjacency_list = adjacency_list
            self.vertices = adjacency_list.keys()
            self.paths = []

We can then define our function which will get a single path from one vetex to another.

This function will accept a source, target, visited dictionary, and target_path list.
The visited and target_path variables will be None by default because we will use these
to keep track of data through a depth first search.


    def get_paths(self, source, target, visited=None, target_path=None):

We start by making local_visited by either making a new dict (if this is the first call of the func)
or making a copy of the list. as well as setting each value related to the vertices to false.

        if visited is None:
            local_visited = {}
            for vertex in self.vertices:
                local_visited[vertex.index] = False
        else:
            local_visited = deepcopy(visited)

We do the same thing with target path

        if target_path is None:
            local_path = []
        else:
            local_path = deepcopy(target_path)

Then, we say that the source has been visied, and append it to the local path.

    local_visited[source.index] = True
        local_path.append(source.data)

If the source is ever equal to the target, we have found one valid path and append the local path
as well as the sum of the local path to the self.paths instance variable.

        if source == target:
            self.paths.append((local_path, sum(local_path)))
        else:

Otherwise, we continue/start our depth first search by making sure there are adjacent nodes.
For each of those adjacent nodes as long as they have not been visited, we will call get_paths
again with our source being the new node we are on, and our target remaining the same.
We also pass in local_visited and local_path to keep track of what has been visited and what
is part of the current path.

            if self.adjacency_list[source.index][1] is not None:
                for i in self.adjacency_list[source.index][1]:
                    if local_visited[i.index] is False:
                        self.get_paths(i, target, local_visited, local_path)

When this function finishes runing, we will have the paths from one node to another saved in
our self.paths instance variable.

We then can simple make a loop that creates a path from every node to every other node
in our list.

        def rebuild_paths(self):
            self.paths = []
            for source in self.vertices:
                for target in self.vertices:
                    self.get_paths(source, target)

After this, it's a simple matter of calling our rebuild_paths function then
checking through our paths and returning a list of the paths that sum to a certain value, if any.

        def find_paths_with_sum(target):
            return_paths = []
            self.rebuild_paths()
            for path in self.paths:
                if path[1] == target:
                    return_paths.append(path[0])
            return return_paths
'''

from copy import deepcopy

class Node:
    def __init__(self, data: any, index: int):
        '''
        A simple node class that has data and an index indicating its location in an array

        Args:
            data: The data that the node holds
            index: The index representing the nodes location in a list
        '''
        self.data = data
        self.index = index

class CheckForPath:
    '''
    Args:
        adjacency_list(list): A list of nodes and what they are adjacent to.
    '''
    def __init__(self, adjacency_list: list):
        self.adjacency_list = adjacency_list
        self.vertices = {item[0]: item[1] for item in adjacency_list}.keys()
        self.paths = []

    def find_paths_with_sum(self, target: int) -> list:
        '''
        Gets all the paths that sum to a certain target value

		Args:
			target: The target value that the paths returned sum up to.

		Returns:
			return_paths: A list of the paths that have values which sum up to the target
				value.
        '''
        return_paths = []
        self.rebuild_paths()
        for path in self.paths:
            if path[1] == target:
                return_paths.append(path[0])
        return return_paths

    def rebuild_paths(self):
        """
        Builds all possible paths in the graph, including singular nodes.
        """
        self.paths = []
        for source in self.vertices:
            for target in self.vertices:
                self.get_paths(source, target)


    def get_paths(
            self,
            source: Node,
            target: Node,
            visited: dict=None,
            target_path: list=None
            ) -> None:
        """
        Obtains list of all paths from u to v, via DFS

        Args:
            source: The starting node of the search from one node to another.
            target: The target node of the search from one node to another.
            visited: Default None, used in recursive calls to keep track of
                nodes that have already been visited.
            target_path: Default None, used in recursive calls to keep track
                of the current path that is being traversed.
        """
        if visited is None:
            local_visited = {}
            for vertex in self.vertices:
                local_visited[vertex.index] = False
        else:
            local_visited = deepcopy(visited)

        if target_path is None:
            local_path = []
        else:
            local_path = deepcopy(target_path)


        local_visited[source.index] = True
        local_path.append(source.data)

        if source == target:
            self.paths.append((local_path, sum(local_path)))
        else:
            if self.adjacency_list[source.index][1] is not None:
                for i in self.adjacency_list[source.index][1]:
                    if local_visited[i.index] is False:
                        self.get_paths(i, target, local_visited, local_path)


def node_generator(data):
    '''
    A generator function that accepts data and returns a new node on each next call.

    Args:
        data: A list of values that will be put into nodes.

    Yields:
        Node: the next node in the list of data, has values data and index.
    '''
    index = -1
    while index < len(data):
        index += 1
        yield Node(data[index], index)


def create_node_list(node_data):
    '''
    Creates a list containing lists of nodes paired with lists of neighbor nodes.

    Args:
        node_data: A list of data that will be converted into an adjacency list of nodes.

    Returns:
        return_list: An adjacency list of nodes relating each node to zero or more neighbors.
    '''
    return_list = [[None, []]] * len(node_data)
    my_gen = node_generator(node_data)
    for i in range(len(return_list)):
        return_list[i] = [next(my_gen), []]

    for i, node in enumerate(return_list):
        if (i * 2) + 1 == len(return_list) - 1:
            node[1].append(return_list[(i * 2) + 1][0])
        elif (i * 2) + 1 > len(return_list) - 1:
            break
        elif i == 0:
            node[1].append(return_list[i + 1][0])
            node[1].append(return_list[i + 2][0])
        elif i == 1:
            node[1].append(return_list[i + 2][0])
            node[1].append(return_list[i + 3][0])
        else:
            node[1].append(return_list[(i * 2) + 1][0])
            node[1].append(return_list[(i * 2) + 2][0])

    return return_list
