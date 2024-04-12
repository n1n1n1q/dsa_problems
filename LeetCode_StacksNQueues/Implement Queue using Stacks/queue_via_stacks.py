"""
Stack class
"""


class Node:
    """
    Node class
    """

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class Stack:
    """
    Stack class
    """

    def __init__(self):
        self.head = None

    def push(self, item):
        """
        Push an element
        """
        if self.head:
            self.head = Node(item, self.head)
        else:
            self.head = Node(item)

    def is_empty(self):
        """
        Checks whether the stack is empty
        """
        return self.head is None

    def pop(self):
        """
        Pops the last element of the stack
        """
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    @property
    def peek(self):
        """
        Peek
        """
        return self.head.data if self.head else None

    def __repr__(self):
        res = "Stack("
        curr = self.head
        while curr is not None:
            res += str(curr.data) + " "
            curr = curr.next
        res += "None)"
        return res

    def __len__(self):
        curr = self.head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length


class MyQueue:

    def __init__(self):
        self.queue = Stack()
        self.tmp = Stack()

    def push(self, x: int) -> None:
        while not self.queue.is_empty():
            self.tmp.push(self.queue.pop())
        self.tmp.push(x)
        while not self.tmp.is_empty():
            self.queue.push(self.tmp.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue.peek

    def empty(self) -> bool:
        return self.queue.is_empty()

    def __repr__(self):
        return repr(self.queue).replace("Stack", "Queue")


queuee = MyQueue()
queuee.push(1)
queuee.push(2)
queuee.push(3)
print(queuee)


print("-----")

stackk = Stack()
stackk.push(1)
stackk.push(2)
print(stackk.pop())
