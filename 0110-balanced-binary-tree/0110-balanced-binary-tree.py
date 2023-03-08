# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxdepth(root):
            left = 0
            right = 0
            if not root:
                return 0
            if root.left:
                left = maxdepth(root.left)
            if root.right:
                right = maxdepth(root.right)
            return max(left,right) + 1
        def check(root):
            if not root:
                return True
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            if right == left:
                return check(root.right) and check(root.left)
            elif right == left + 1:
                return check(root.right) and check(root.left)
            elif right + 1 == left:
                return check(root.right) and check(root.left)
            else:
                return False
            return check(root.right) and check(root.left)
        return check (root)
        
        