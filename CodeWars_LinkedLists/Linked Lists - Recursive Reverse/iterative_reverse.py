class Node(object):
    def __init__(self, data=None, nextt=None):
        self.data = data
        self.next = nextt


def reverse(head):
    prev = None
    next_ = 0
    while next_ is not None:
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
    head = prev
    return prev


if __name__ == "__main__":

    def print_node(node):
        while node is not None:
            print(node.data if not node is None else "", end=" ")
            node = node.next
        print(node)

    ll = Node(1, Node(2, Node(3)))
    print_node(reverse(ll))
    print_node(ll)
    print()
    print_node(reverse(Node(2, Node(1, Node(3, Node(6, Node(5)))))))
