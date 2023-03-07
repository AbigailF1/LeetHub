# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        
        def find_root(root):
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            if right == left:
                return root
            if right > left:
                return find_root(root.right)
            if right < left:
                return find_root(root.left)
            
        return find_root(root)