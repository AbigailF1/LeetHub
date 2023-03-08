# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(root, update):
            if not root:
                return 0
            if not root.right and not root.left:
                root.val += update
                return root.val
            if root.right:
                new_value = inorder(root.right,update)
                root.val += new_value
            else:
                root.val += update
            if root.left:
                return inorder(root.left, root.val)
            return root.val
        inorder(root, 0)
        return root
        