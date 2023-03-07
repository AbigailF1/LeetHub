# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(Node, minimum = -inf, maximum = inf):
            if not Node:
                return True 
            if Node.val <= minimum or Node.val >= maximum:
                return False 
            left_validity= validity(Node.left, minimum, Node.val)
            right_validity = validity(Node.right, Node.val, maximum)
            return left_validity and right_validity 
        return validity(root)
        