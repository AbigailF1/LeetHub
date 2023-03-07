# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            left = []
            right = []
            if not root :
                return []
            if root.left:
                left = inorderTraversal(root.left)
            if root.right:
                right = inorderTraversal(root.right)
            return left + [root.val] + right
        arr = inorderTraversal(root)
        if (all(i < j for i, j in zip(arr, arr[1:]))):
            if arr == sorted(arr) :

                return True
            else:
                return False
        return False