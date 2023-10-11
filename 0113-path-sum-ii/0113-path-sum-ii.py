# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res  = []
        
        def path(root, sum_, arr):
            
            if not root:
                return 
            
            if not root.left  and not root.right:
                if sum_ + root.val  == targetSum:
                    res.append(arr + [root.val])
                    return 
    
            path(root.left,sum_ + root.val, arr + [root.val])
            path(root.right,sum_ + root.val, arr + [root.val])
                     

        path(root, 0, []) 
        
        return res
        