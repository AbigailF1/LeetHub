# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def traverse(root, row, column, dic):
            if not root:
                return 
            dic[column].append([row, root.val])
            traverse(root.right, row + 1, column + 1,dic)
            traverse(root.left, row + 1 , column - 1, dic)
        traverse(root, 0, 0 , dic)
        ans = []
        
        for i, j in sorted(dic.items()):
            j.sort()
            nums = []
            for row, val in j:
                nums.append(val)
            ans.append(nums)
        return ans
        
        