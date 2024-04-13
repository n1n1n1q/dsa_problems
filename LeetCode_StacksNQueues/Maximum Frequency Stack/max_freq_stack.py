"""
Max frequency stack
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.frequency = 1

    def __repr__(self):
        return f"Node(data = {self.data}, frequency = {self.frequency})"


class FreqStack:
    def __init__(self):
        self.head = None
        self.max_freq = 0

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            self.max_freq = 1
        else:
            self.head = Node(val, self.head)
            curr = self.head.next
            while curr is not None:
                if curr.data == self.head.data:
                    self.head.frequency += curr.frequency
                    break
                curr = curr.next
            if self.head.frequency > self.max_freq:
                self.max_freq = self.head.frequency

    def pop(self):
        curr = self.head
        res = 0
        self.max_freq -= 1
        if curr.frequency == self.max_freq + 1:
            res = self.head.data
            self.head = self.head.next
        else:
            while curr.next is not None:
                if curr.next.frequency == self.max_freq + 1:
                    res = curr.next.data
                    curr.next = curr.next.next
                    break
                curr = curr.next
        curr = self.head
        while curr is not None:
            if curr.frequency > self.max_freq:
                self.max_freq = curr.frequency
                return res
            curr = curr.next
        return res

    def __str__(self):
        curr = self.head
        res = f"Frequency Stack, max frequency = {self.max_freq}, "
        while curr.next is not None:
            res += str(curr) + " -> "
            curr = curr.next
        res += str(curr)
        return res


if __name__ == "__main__":
    stack = FreqStack()
    lst = [5, 7, 5, 7, 4, 5]
    for i in lst:
        stack.push(i)
    print(stack)
    print(stack.pop())
    print(stack)
    for i in range(4):
        print(stack.pop())
