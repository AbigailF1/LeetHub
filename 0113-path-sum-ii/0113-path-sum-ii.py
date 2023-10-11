# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res  = []
        
        if root:
            start = root.val
            
        def path(root, targetsum, arr):
            nonlocal start
            nonlocal res
            
            if not root:
                return 
            
            arr.append(root.val)
            ans = 0
            # print(root.val,  not root.left  and root.right )
            if not root.left  and not root.right:
                for i in range(len(arr) -1, -1, -1):
                    ans += arr[i]
                if ans == targetsum:
                    # print(arr)
                    if arr[i] == start :
                        res.append(arr[i:])

            # print(res)     
            path(root.left,targetsum, arr)
            path(root.right,targetsum, arr)
            arr.pop()           

        path(root, targetSum, []) 
        
        return res
        