# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def path(root, targetsum, arr):
            nonlocal count
            if not root:
                return 
            arr.append(root.val)
            ans = 0
            # print(arr)
            for i in range(len(arr) -1, -1, -1):
                ans += arr[i]
                if ans == targetsum:
                    count += 1
            path(root.left,targetsum, arr)
            path(root.right,targetsum, arr)
            arr.pop()           

        path(root, targetSum, []) 
        return count
       
        