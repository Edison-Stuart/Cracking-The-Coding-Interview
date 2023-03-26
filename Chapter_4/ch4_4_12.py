'''
You are given a binary tree where each node contains an integer value (positive OR negative)
Design an algorithm to count the number of paths that sum to a given value. The path does not need
to start at the root or end at a leaf but it must only travel downwards.
'''

from copy import deepcopy

class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index

class CheckForPath:
    '''
    Args:
        adjacency_list(dict): A dictionary of nodes and what they are adjacent to.
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
        """Rebuild all paths for the graph"""
        self.paths = []
        for source in self.vertices:
            for target in self.vertices:
                self.get_paths(source, target)


    def get_paths(self, source, target, visited=None, target_path=None):
        """Obtains list of all paths from u to v, via DFS"""
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
    index = -1
    while index < len(data):
        index += 1
        yield Node(data[index], index)


def create_node_list(node_data):
    return_list = [[None, []]] * len(node_data)
    my_gen = node_generator(node_data)
    for i in range(len(return_list)):
        next_node = next(my_gen)
        return_list[i] = [next_node, []]

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




if __name__ == "__main__":
    my_list = create_node_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    my_tree = CheckForPath(my_list)
    print(my_tree.find_paths_with_sum(15))
