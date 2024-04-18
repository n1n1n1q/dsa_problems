"""
LL task 6
"""


class Node(object):
    """
    Noed
    """

    def __init__(self, data, nextt=None):
        self.data = data
        self.next = nextt


def sorted_insert(head, data):
    """
    Sorted insert
    """
    curr = head
    if head is None:
        return Node(data)
    if data < head.data:
        curr = Node(data)
        curr.next = head
        return curr
    while curr.next is not None:
        if curr.data <= data and data <= curr.next.data:
            tmp = Node(data)
            tmp.next = curr.next
            curr.next = tmp
            return head
        curr = curr.next
    curr.next = Node(data)
    return head
