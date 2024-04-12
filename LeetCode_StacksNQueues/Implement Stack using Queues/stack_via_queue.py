"""
Implementing stack with queue
"""


class Node:
    """
    Node class
    """

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item.data
        return None

    @property
    def peek(self):
        return self.head.data


class MyStack:

    def __init__(self):
        self.stack = Queue()
        self.tmp = Queue()

    def push(self, x: int) -> None:
        self.tmp.add(x)
        while not self.stack.is_empty():
            self.tmp.add(self.stack.pop())
        self.stack = self.tmp
        self.tmp = Queue()
        # while not self.tmp.is_empty():
        #     self.stack.add(self.tmp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack.peek

    def empty(self) -> bool:
        return self.stack.is_empty()
