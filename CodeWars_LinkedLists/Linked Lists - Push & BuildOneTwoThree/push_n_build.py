"""
LL problem 3
"""


# from preloaded import Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    node_ = Node(data)
    node_.next = head
    return node_


def build_one_two_three():
    node_ = None
    for i in [3, 2, 1]:
        node_ = push(node_, i)
    return node_
