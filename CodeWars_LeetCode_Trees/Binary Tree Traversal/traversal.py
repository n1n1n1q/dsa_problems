# Pre-order traversal
def pre_order(node, lst = None):
    if lst is None:
        lst = []
    if node:
        lst.append(node.data)
        pre_order(node.left, lst)
        pre_order(node.right, lst)
    return lst


# In-order traversal
def in_order(node, lst = None):
    if lst is None:
        lst = []
    if node:
        in_order(node.left, lst)
        lst.append(node.data)
        in_order(node.right, lst)
    return lst

# Post-order traversal
def post_order(node, lst = None):
    if lst is None:
        lst = []
    if node:
        post_order(node.left, lst)
        post_order(node.right, lst)
        lst.append(node.data)
    return lst
