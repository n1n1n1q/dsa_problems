class Node(object):
    def __init__(self, data=None, ne=None):
        self.data = data
        self.next = ne


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise Exception
    even = None
    odd = None
    it = 1
    while head is not None:
        if it & 1:
            if odd is None:
                odd = head
                l = odd
            else:
                print(odd.data, " -> ", head.data)
                odd.next = head
                odd = head
        else:
            if even is None:
                even = head
                r = even
            else:
                even.next = head
                even = head
        it += 1
        head = head.next
    odd.next = None
    even.next = None
    return Context(l, r)


if __name__ == "__main__":

    def print_node(node):
        while node is not None:
            print(node.data if not node is None else "", end=" ")
            node = node.next

    c = alternating_split(Node(1, Node(2, Node(3, Node(4)))))
    print_node(c.first)
    print("\n")
    print_node(c.second)
