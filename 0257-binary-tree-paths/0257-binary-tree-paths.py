# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def list_maker(root):
            list_right = []
            list_left =[]
            if not root:
                return 
            if not root.left and not root.right:
                return [[str(root.val)]]
            if root.right:
                list_right = list_maker(root.right)
            if root.left:
                list_left = list_maker(root.left)
            main_list = list_left + list_right
            for i in range(len(main_list)):
                main_list[i].append(str(root.val))
            return main_list
        ans_list = list_maker(root)
        ans = []
        for i in range(len(ans_list)):
            ans.append("->".join(reversed(ans_list[i])))
        return ans 
                
            
        
            
            