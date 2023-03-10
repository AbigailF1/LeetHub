# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def traversal(root, depth):
            if not root:
                return 
            d[depth].append(root.val)
            traversal(root.left, depth+1)
            traversal(root.right, depth+1)
            return 
        traversal(root, 0)
        return (d.values())
            
        