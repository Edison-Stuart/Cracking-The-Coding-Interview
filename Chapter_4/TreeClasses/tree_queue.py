'''
This module holds the class Queue and the class QueueNode
and is used for building a queue data structure.
'''

class QueueNode:
    """Class that creates a node with data to be used in a queue"""
    def __init__(self, data: any):
        """
		Args:
			data: The data that will be stored in the queue node
		"""
        self.data = data
        self.next = None

class Queue:
    """Class for implementing a Queue of items"""

    def __init__(self):
        """Creates an empty queue with the first and last values"""
        self.first = None
        self.last = None

    def enqueue(self, data: any) -> None:
        """
		Adds a node to the end of the queue

		Args:
			data: The data that will be put into a QueueNode then
				added to the Queue
		"""
        temp = QueueNode(data)
        if self.last is not None:
            self.last.next = temp
        self.last = temp
        if self.first is None:
            self.first = self.last

    def dequeue(self) -> any:
        """
		Removes one node from the front of the queue

		Returns:
			data (any): The first element of the queue

		Raises:
			Exception: if no element is in the queue
		"""
        if self.first is None:
            raise Exception("No such element in queue")

        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return data

    def peek(self) -> any:
        """
		gets the first element back from the queue without removing it

		Returns:
			data (any): The data from the first element of the queue

		Raises:
			Exception: if no element is in the queue
		"""
        if self.first is None:
            raise Exception("No such element in queue")
        return self.first.data

    def is_empty(self) -> bool:
        """
		Checks if a queue is empty

		Returns:
			bool: True if the queue is empty, false otherwise.
		"""
        return self.first is None
