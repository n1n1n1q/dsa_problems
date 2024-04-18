class Node(object):
    def __init__(self, data=None, nextt=None):
        self.data = data
        self.next = nextt


def reverse(head, prev=None):
    if head is None:
        return head
    if head.next is None:
        head.next = prev
        return head
    next = reverse(head.next, head)
    head.next = prev
    return next


if __name__ == "__main__":

    def print_node(node):
        while node is not None:
            print(node.data if not node is None else "", end=" ")
            node = node.next

    print_node(reverse(Node(1, Node(2, Node(3)))))
    print()
    print_node(reverse(Node(1, Node(3))))
