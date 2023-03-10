# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def traverse(root):
            if not root:
                return 
            
            ans.append(root.val)
            traverse(root.right)
            traverse(root.left)
            
        traverse(root)
        
        count = collections. Counter(ans)
        max_mode = max(count.values())
        mode = []
        for c in count:
            if count[c] == max_mode:
                mode.append(c)
        return mode
        
        
        
        
        
        