# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        def find_target(root, tar):
            if not root:
                return False 
            if root == tar:
                return True 
            return find_target(root.right, tar) or find_target(root.left, tar)
            
        def find_root(root, t, k):
            length = 0
            if not root: 
                return 
            if root == t:
                opr(root, k)
                return k-1
            if find_target(root.right, t):
                length = find_root(root.right, t, k)
                if length == 0:
                    self.ans.append(root.val)
                opr(root.left, length-1)
            if find_target(root.left,t):
                length = find_root(root.left, t, k)
                if length == 0:
                    self.ans.append(root.val)
                opr(root.right, length-1)          
            return length - 1
        def opr(root,k): 
            if not root or k < 0: 
                return 
         
            if k == 0: 
                self.ans.append(root.val) 
                return 
             
            opr(root.left,k-1) 
            opr(root.right,k-1) 
             
        find_root(root,target,k) 
        return self.ans
                
            