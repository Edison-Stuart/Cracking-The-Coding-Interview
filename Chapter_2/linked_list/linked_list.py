'''Contains class that uses Nodes to create a linked list based on parameters'''
from .list_node import Node
class LinkedList:
    '''Class that uses Nodes to create a linked list based on parameters'''
    def __init__(self, *args):
        self.head_node = None
        for i, item in enumerate(args):
            if i == 0:
                self.head_node = Node(item)
            else:
                self.head_node.append_to_tail(item)

    def add_to_list(self, item):
        '''Accepts item and appends it to the Node list'''
        self.head_node.append_to_tail(item)

    def get_all_nodes(self):
        '''Returns all nodes in current Node list'''
        node_list = [str(self.head_node)]
        current_node = self.head_node
        while current_node.next_node is not None:
            node_list.append(str(current_node.next_node))
            current_node = current_node.next_node
        return node_list

    def get_specific_node(self, user_index):
        '''Returns a specific node from the list using an index'''
        current_node = self.head_node
        target_node = None
        search_index = 0
        while target_node is None:
            if search_index == user_index:
                target_node = current_node
            elif current_node.next_node is not None:
                current_node = current_node.next_node
                search_index += 1
            else:
                return -1
        return target_node


def delete_from_linked_list(head_node, target):
    '''Accepts the head node of a linked list and the target
       value you want removed. Returns the head of a new linked list'''
    if head_node is None:
        return None

    current_node = head_node
    if current_node.data == target:
        return head_node.next_node

    while current_node.next_node is not None:
        if current_node.next_node.data == target:
            current_node.next_node = current_node.next_node.next_node
            return head_node
        current_node = current_node.next_node
    return head_node


if __name__ == '__main__':
    linked_list = LinkedList(4, 6, 1, 7, 8, 0, 200, 45, 124, 5233)
    print(linked_list.get_all_nodes())
    linked_list.head_node = delete_from_linked_list(linked_list.head_node, 0)
    print(linked_list.get_all_nodes())
