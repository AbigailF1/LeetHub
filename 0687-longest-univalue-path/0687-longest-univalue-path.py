# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def longest(root, parent):
            if not root:
                return 0 
            left = longest(root.left, root.val)
            right = longest (root.right, root.val)
            
            self.ans = max(self.ans, left + right)
            
            if root.val!= parent:
                return 0
            else:
                return max(left, right) + 1
            
        longest(root, -2000)  
        return self.ans