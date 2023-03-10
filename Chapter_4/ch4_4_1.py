'''
Given a directed graph and two nodes, S and E, design an algorithm to
find out whether there is a route from S to E.
'''
from copy import deepcopy

class CheckForPath:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.vertices = adjacency_list.keys()
        self.paths = []

    def get_paths(self, source, target, visited=None, target_path=None):
        """Obtains list of all paths from S to E, via DFS"""
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
                self.paths.append(local_path)
            else:
                if self.adjacency_list[source] is not None:
                    for i in self.adjacency_list[source]:
                        if local_visited[i] is False:
                            self.get_paths(i, target, local_visited, local_path)

        except Exception as error:
            raise Exception('While obtaining paths: %s' % error)

    def is_path_present(self, source, target):
        return_value = None
        try:
            self.get_paths(source, target)
            if self.paths:
                return_value = True
            else:
                return_value = False
        except Exception as err:
            raise Exception(str(err))
        return return_value
