from edge import Edge
from ..TreeClasses.tree_queue import Queue

class GraphNode:
    def __init__(self, data=None):
        self.data = data
        self.edges = [None, None, None]

def build_graph(data):
    head_node = GraphNode(data[0])
    current_node = head_node
    nodes_to_be_filled = Queue()
    total_nodes = 1
    cur_index = 1
    while total_nodes < len(data) or not nodes_to_be_filled.is_empty():
        if current_node.data is None:
            current_node.data = data[cur_index]
            cur_index += 1

        if current_node.edges[1] is None and current_node.edges[2] is None:
            if total_nodes == len(data):
                current_node = nodes_to_be_filled.dequeue()
            elif total_nodes + 2 <= len(data):
                left_edge = Edge(current_node, GraphNode(None))
                right_edge = Edge(current_node, GraphNode(None))
                total_nodes += 2

                current_node.edges[1] = left_edge
                current_node.edges[2] = right_edge

                next_nodes = [
                    current_node.edges[1].vertices[1],
                    current_node.edges[2].vertices[1]
                    ]
                print('got here')
                next_nodes[0].edges[0] = left_edge
                next_nodes[1].edges[0] = right_edge

                nodes_to_be_filled.enqueue(next_nodes[0])
                nodes_to_be_filled.enqueue(next_nodes[1])

                current_node = nodes_to_be_filled.dequeue()
            else:
                left_edge = Edge(current_node, GraphNode(None))
                total_nodes += 1

                current_node.edges[1] = left_edge

                next_node = current_node.edges[1].vertices[1]
                next_node.edges[0] = current_node

                nodes_to_be_filled.enqueue(next_node)
                current_node = nodes_to_be_filled.dequeue()

    if len(data) != 1:
        current_node.data = data[cur_index]

    return head_node
