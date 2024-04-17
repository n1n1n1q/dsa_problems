class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    queue = [node]
    res = []
    while queue:
        curr = queue.pop(0)
        if curr:
            queue.append(curr.left)
            queue.append(curr.right)
            res.append(curr.value)
    return res
