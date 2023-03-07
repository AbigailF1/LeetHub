# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(r_part, l_part):
            if not r_part and not l_part:
                return True 
            if not r_part and l_part:
                return False
            if r_part and not l_part:
                return False
            checked = check(l_part.left, r_part.right) and check(l_part.right, r_part.left)
            return r_part.val == l_part.val and checked 
        return check(root.left, root.right)
        