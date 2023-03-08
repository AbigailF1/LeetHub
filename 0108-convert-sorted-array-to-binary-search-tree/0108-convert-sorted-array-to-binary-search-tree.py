# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BSTT(root, left, right):
            if left == right:
                return None
            if right == 1:
                return TreeNode(nums[0])
            mid = (left + right)//2
            root = TreeNode(nums[mid])
            root.left = BSTT(root, left, mid)
            root.right =BSTT(root, mid+1, right)
            return root
        return BSTT(nums, 0 , len(nums))
