# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def evenSumm(node, parent, grandparent):
            answer = 0
            if not node:
                return 0
            if grandparent % 2 == 0:
                answer += node.val
            answer += evenSumm(node.left, node.val, parent)
            answer += evenSumm(node.right, node.val, parent)
            return answer
        return evenSumm(root,1,1)