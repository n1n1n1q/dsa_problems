"""
LL Problem 2
"""


class Node:
    """Node"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"


def linked_list_from_string(s):
    """
    LL from str
    """
    string = s.split(" -> ")
    if len(string) == 1:
        return None
    first = Node(int(string[0].strip()))
    tmp = first
    for i in range(1, len(string) - 1):
        string[i] = string[i].strip()
        tmp.next = Node(int(string[i]))
        tmp = tmp.next
    return first


if __name__ == "__main__":
    nodee = linked_list_from_string("1 -> 2 -> None")
    while nodee != None:
        print(type(nodee.data))
        nodee = nodee.next
    assert nodee == Node(1, Node(2))
