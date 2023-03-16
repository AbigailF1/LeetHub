# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        count = 0
        def traverse(root):
            if not root:
                return
            self.ans.append(root.val)
            traverse(root.left)
            traverse(root.right)
        def compute(root):
            nonlocal count 
            if not root:
                return
            self.ans = []
            traverse(root)
            if self.ans[0] == sum(self.ans)// len(self.ans):
                count += 1
            compute(root.left)
            compute(root.right)
        compute(root)
        return count
                
            
            
            
            
        