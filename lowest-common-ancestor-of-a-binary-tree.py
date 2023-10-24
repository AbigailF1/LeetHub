# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(node):
            if not node:
                return [False, None]
            
            left , l_node = traverse(node.left)
            right , r_node = traverse(node.right)
            
            if node == p or node == q:
                if left or right:
                    return [True, node]
                return [True, None]
            else:
                if left and right:
                    return [True, node]
                elif left or right:
                    return [True, l_node if left else r_node]
            return [False, None]
        return traverse(root)[1]