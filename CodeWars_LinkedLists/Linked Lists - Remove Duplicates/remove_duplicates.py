class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates(head):
    if head is None:
        return head
    duplicates = set()
    curr = head
    prev = None
    while curr is not None:
        if curr.data in duplicates:
            prev.next = curr.next
        else:
            duplicates.add(curr.data)
            prev = curr
        curr = curr.next
    return head


if __name__ == "__main__":

    def print_node(node):
        while node is not None:
            print(node.data if not node is None else "", end=" ")
            node = node.next

    print_node(
        remove_duplicates(Node(1, Node(2, Node(3, Node(3, Node(4, Node(4, Node(5))))))))
    )
