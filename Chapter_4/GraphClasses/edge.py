class Edge:
    def __init__(self, node1=None, node2=None):
        self.vertices = [node1, node2]
        self.marked_by = []
