# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(root):
            left = []
            right = []
            if not root:
                return []
            if not root.right and not root.left:
                right = []
                left = []
            elif not root.right:
                right = [None]
            elif not root. left:
                left = [None]
            if root.right:
                right = check(root.right)
            if root. left:
                left = check(root.left)
            return [root.val] + left + right
            print [root.val] + left + right
        return check(p) ==check(q)
        