# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def tree(List):
            if len(List) == 0:
                return 
            if len(List) == 1:
                return TreeNode(List[-1])
            root = TreeNode(List[0])  
            indx = bisect_left(List[1:], List[0]) + 1
            root.left = tree(List[1:indx])
            root.right = tree(List[indx:]) 
            return root    
        return tree(preorder)
                    
                
                
                
        