# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.val = self.swap_value(root.right)
            root.right = self.deleteNode(root.right,root.val)
        return root
    def swap_value(self, root):
        val = root.val
        while root.left is not None:
            root = root.left
            val = root.val
        return val
    #     self.root = root
    #     prev, curr = self.search(key)
    #     if not prev:
    #         return root
    #     if curr.left and not curr.right:
    #         if prev.left == curr:
    #             prev.left = curr.left
    #         else:
    #             prev.left = curr.right
    #     elif curr.right and not curr.left:
    #         if prev.left == curr:
    #             prev.left = curr.right
    #         else:
    #             prev.right = curr.right
    #     else:
    #         new = curr
    #         prev_new = None
    #         while new.right is not None:
    #             prev_new = new
    #             new = new.right
    #         print(prev_new.val, new.val)
    #         if prev.left == curr:
    #             prev.left = new
    #         else:
    #             prev.right = new
    #         prev_new.right = None    
    #         new.right = curr.right
    #         new.left = curr.left
    #     return root

    # def search(self, val):
    #     curr = self.root
    #     prev = None
    #     while curr:
    #         if curr.val == val:
    #             return prev, curr
    #         prev = curr
    #         if curr.val < val:
    #             curr = curr.right
    #         else:
    #             curr = curr.left
    #     return None, None