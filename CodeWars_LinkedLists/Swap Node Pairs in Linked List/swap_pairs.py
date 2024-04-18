class Node:
    def __init__(self, next):
        self.next = next


def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = head
    curr = head.next
    head = curr
    while 1:
        next_ = curr.next
        curr.next = prev
        if next_ is None:
            prev.next = None
            return head
        if next_.next is None:
            prev.next = next_
            return head
        prev.next = next_.next
        prev = next_
        curr = prev.next
    return head
