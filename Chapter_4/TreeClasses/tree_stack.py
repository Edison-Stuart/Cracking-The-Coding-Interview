'''A stack class implemented in python.'''

class StackNode:
    '''Creates an object to be used as a node in a stack.'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''Uses StackNodes to hold data in last-in-first-out ordering.'''
    def __init__(self):
        self._top = None

    def push(self, data):
        """Puts an item on to the top of the stack."""
        if self._top is None:
            self._top = StackNode(data)
        else:
            temp = StackNode(data)
            temp.next = self._top
            self._top = temp

    def pop(self):
        """Removes the top item from the stack and returns it."""
        if self._top is None:
            item = None
        else:
            item = self._top.data
            self._top = self._top.next
        return item

    def peek(self):
        """Returns the top item of the stack"""
        if self._top is None:
            item = None
        else:
            item = self._top.data
        return item

    def is_empty(self):
        """Returns true if stack is empty"""
        return bool(self._top is None)
