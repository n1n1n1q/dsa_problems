"""
LL task1
"""


def stringify(node):
    """
    Stringify
    """
    res = ""
    if node is None:
        return "None"
    while node is not None:
        res += str(node.data) + " -> "
        node = node.next
    res += str(node)
    return res
