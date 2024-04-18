class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if source is None:
        raise Exception
    dest = Node(source.data, dest)
    source = source.next
    return Context(source, dest)


def print_node(node):
    while node is not None:
        print(node.data if isinstance(node, Node) else "", end=" ")
        node = node.next


if __name__ == "__main__":
    c = move_node(Node(1, Node(2, Node(10101))), Node(1, Node(121, Node(31))))
    print_node(c.dest)
    print()
    print_node(c.source)
