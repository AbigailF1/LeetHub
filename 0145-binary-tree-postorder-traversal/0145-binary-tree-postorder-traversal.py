# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        left =[]
        right =[]
        if not root:
            return []
        if root.left:
            left = self.postorderTraversal(root.left)
        if root.right:
            right = self.postorderTraversal(root.right)
        return left + right +[root.val]
            
        
        