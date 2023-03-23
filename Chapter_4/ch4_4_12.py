'''
You are given a binary tree where each node contains an integer value (positive OR negative)
Design an algorithm to count the number of paths that sum to a given value. The path does not need
to start at the root or end at a leaf but it must only travel downwards.
'''

from copy import deepcopy

class CheckForPath:
    '''
    Args:
        adjacency_list(dict): A dictionary of nodes and what they are adjacent to.
    '''
    def __init__(self, adjacency_list: dict):
        self.adjacency_list = adjacency_list
        self.vertices = self.adjacency_list.keys()
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
        try:
            self.paths = []
            for source in self.vertices:
                for target in self.vertices:
                    self.get_paths(source, target)

        except Exception as error:
            raise Exception('While rebuilding paths: %s' % error)

    def get_paths(self, source, target, visited=None, target_path=None):
        """Obtains list of all paths from u to v, via DFS"""
        try:
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
                raise Exception(
                    'Cycle present in path; ' +
                    'source %s neighbors %s intersect path %s' %
                    (source, self.adjacency_list[source], local_path)
                )

            local_visited[source] = True
            local_path.append(source)

            if source == target:
                self.paths.append((local_path, sum(local_path)))
            else:
                if self.adjacency_list[source] is not None:
                    for i in self.adjacency_list[source]:
                        if local_visited[i] is False:
                            self.get_paths(i, target, local_visited, local_path)

        except Exception as error:
            raise Exception('While obtaining paths: %s' % error)

if __name__ == "__main__":
    my_graph = CheckForPath()
    print(my_graph.find_paths_with_sum(15))
    # print(my_graph.paths)
