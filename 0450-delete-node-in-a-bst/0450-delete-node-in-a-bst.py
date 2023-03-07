# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorder(Node): # only for finding the min of the left part of the tree
            current = Node
            while current.right:
                current = current. right
            return current 
        if not root:
            return root 
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # for node that has two children
            new_key = inorder(root.left)
            root.val = new_key.val
            root.left = self.deleteNode(root.left, new_key.val)
        return root
            