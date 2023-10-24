# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        def traverse(root, width, depth):
            if not root:
                return 
            dic[depth].append(width)
            traverse(root.left,2*width ,depth+1)
            traverse(root.right,2*width+1 ,depth+1)
        traverse(root, 1, 0)
        maximum = 0 
        for i in dic:
            maximum = max(maximum, max(dic[i]) - min(dic[i]) + 1)
        return maximum