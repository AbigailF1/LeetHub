# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            with_split = left + right + root.val
            without_split = root.val + max(left, right)
            ans = max(ans, with_split)
            return without_split
            
        dfs(root)      
        return ans
                
            
    
        
        