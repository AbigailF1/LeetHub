# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(r_part, l_part):
            if not r_part and not l_part:
                return True 
            
            if (not r_part and l_part) or (r_part and not l_part):
                return False
            
            if r_part.val != l_part.val:
                return False
            
            checked = check(l_part.left, r_part.left) and check(l_part.right, r_part.right)
            return checked
        
        def traverse(r_part, l_part):
            if not r_part:
                return False
            if check(r_part, l_part):
                return True 
            return  traverse(r_part.left, l_part) or traverse(r_part.right, l_part) 
        return traverse(root, subRoot)

        
        
        