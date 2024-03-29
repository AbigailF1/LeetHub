# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, pos):
            nonlocal ans 
            if not root:
                return 
            if not root.left and not root.right and pos:
                ans += root.val 
            dfs(root.left, 1)
            dfs(root.right, 0)
        dfs(root, 0)
        return ans 



            
        