"""
LL problem 4
"""

# from preloaded import Node


class Node(object):
    """Node class for reference"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    idx = 0
    while node is not None and index != idx:
        idx += 1
        node = node.next
    if node is None:
        raise Exception
    return node
