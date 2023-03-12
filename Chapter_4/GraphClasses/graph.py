from .edge import Edge
from ..TreeClasses.tree_queue import Queue

class GraphNode:
    def __init__(self, data=None):
        self.data = data
        self.edges = [None] * 3

def create_new_connected_edge(node: GraphNode) -> Edge:
    '''
    Creates a new edge connected to a current node and a new graph node

    Args:
        node(GraphNode): The node that will be connected to the first
            vertex of the Edge object.

    Returns:
        Edge: A new Edge object that has stored in the vertices array
            at vertices[0], the node, and at vertices[1], the new GraphNode

    Raises:
        TypeError: If node is not of type GraphNode
    '''
    if isinstance(node, GraphNode) is False:
        raise TypeError(
            f'create_new_connected_edge only accepts Type: GraphNode. Recieved {type(node)}'
            )

    return Edge(node, GraphNode(None))

def add_previous_edge(node: GraphNode, previous_edge: Edge) -> None:
    '''
    Adds an edge to node.edges[0]

    Args:
        node(GraphNode): The node that will be getting a previous edge added
            to it.
        previous_edge(Edge): An edge object that already has a reference to the node,
            This edge will be added to the nodes index 0 edge.

    Raises:
        TypeError: If node is not of type GraphNode.
        TypeError: If previous_edge is not of type Edge.
    '''
    if isinstance(node, GraphNode) is False:
        raise TypeError(
            f'add_previous_edge only accepts node of Type: GraphNode. Recieved {type(node)}'
        )
    if isinstance(previous_edge, Edge) is False:
        raise TypeError(
            f'add_previous_edge only accepts previous_edge of Type: Edge. Recieved {type(node)}'
        )
    node.edges[0] = previous_edge

def add_two_nodes(node: GraphNode, queue: Queue):
    '''
    Creates two new edges and GraphNodes attatched to them, and adds the new nodes to
        a queue.

    Args:
        node(GraphNode): The current node whos edges will be getting added to.
        queue(Queue): The Queue that the new nodes will be added to.

    Returns:
        queue: The queue that was sent in and added to.

    Raises:
        TypeError: If node is not of type GraphNode
        TypeError: If queue is not of type Queue
    '''
    if isinstance(node, GraphNode) is False:
        raise TypeError(
            f'add_two_nodes only accepts node of Type: GraphNode. Recieved {type(node)}'
        )
    if isinstance(queue, Queue) is False:
        raise TypeError(
            f'add_two_nodes only accepts queue of Type: Queue. Recieved {type(queue)}'
        )

    node.edges[1] = create_new_connected_edge(node)
    node.edges[2] = create_new_connected_edge(node)

    next_nodes = (
        node.edges[1].vertices[1],
        node.edges[2].vertices[1]
    )

    add_previous_edge(next_nodes[0], node.edges[1])
    add_previous_edge(next_nodes[1], node.edges[2])

    queue.enqueue(next_nodes[0])
    queue.enqueue(next_nodes[1])

    return queue

def build_graph(data):
    '''
    Will create a graph of nodes and edges given a list of data.

    Args:
        data(list): A list of data, can be of any type, to be stored in
            the graph

    Returns:
        head_node(GraphNode): The 'root node' of a graph object that is build like
            a tree.

    Raises:
	    TypeError: If type of data passed in is not list.
	    Exception: If list passed in is empty.
	'''
    if not isinstance(data, list):
        raise TypeError('Data type must be list')
    if not data:
        raise Exception("No data in list")

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
                total_nodes += 2
                add_two_nodes(current_node, nodes_to_be_filled)
                current_node = nodes_to_be_filled.dequeue()

            else:
                total_nodes += 1
                current_node.edges[1] = create_new_connected_edge(current_node)
                next_node = current_node.edges[1].vertices[1]
                add_previous_edge(next_node, current_node.edges[1])
                nodes_to_be_filled.enqueue(next_node)
                current_node = nodes_to_be_filled.dequeue()

    if len(data) != 1:
        current_node.data = data[cur_index]

    return head_node
