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
            return
        temp = StackNode(data)
        temp.next = self._top
        self._top = temp

    def pop(self):
        """Removes the top item from the stack and returns it."""
        if self._top is None:
            return None
        item = self._top.data
        self._top = self._top.next
        return item

    def peek(self):
        """Returns the top item of the stack"""
        if self._top is None:
            return None
        return self._top.data

    def is_empty(self):
        """Returns true if stack is empty"""
        return bool(self._top is None)

if __name__ == "__main__":
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push("apples")
    my_stack.push("oranges")
    my_stack.push("grapes")
    my_stack.push("grenades")
    my_stack.push("apes")
    print(my_stack.is_empty())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.peek())
