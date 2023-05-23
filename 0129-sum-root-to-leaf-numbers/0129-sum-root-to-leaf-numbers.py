# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, num):
            nonlocal summ
            if not root:
                return 0
            num += str(root.val)
            if not root.left and not root.right:
                summ += int(num)
                return summ
            elif root.left and root.right:
                dfs(root.left, num)
                dfs(root.right,num)
            elif root.left:
                dfs(root.left, num)
            elif root.right:
                dfs(root.right,num)
            
            return 
        
        summ = 0
        dfs(root, "")
        return summ
            
        