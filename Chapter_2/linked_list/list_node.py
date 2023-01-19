'''Contains class that defines a Node meant to be in a linked list'''
class Node:
    '''Class that defines a Node meant to be in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def append_to_tail(self, data):
        '''Appends a node to the tail of the linked list.'''
        end = Node(data)
        this_node = self
        while this_node.next_node is not None:
            this_node = this_node.next_node
        this_node.next_node = end

    def __str__(self):
        return str(self.data)

    def __getitem__(self, item):
        return self.data[item]
