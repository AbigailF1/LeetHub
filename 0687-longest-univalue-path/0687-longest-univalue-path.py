# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def longest(root):
            if not root:
                return 0 
            left = longest(root.left)
            right = longest (root.right)
            left_val = right_val = 0
            if root.right and root.right.val == root.val:
                right_val = right + 1
                
            if root.left and  root.left.val == root.val:
                left_val = left + 1 
            self.ans = max(self.ans, left_val + right_val)
            return max(left_val, right_val)  
        longest(root)  
        return self.ans