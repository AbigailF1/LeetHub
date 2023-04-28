# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = []
        queue = deque([root])
        
        while queue:
            summ = 0
            n = len(queue)
            for i in queue:
                summ += i.val
            arr.append(summ/ len(queue))
            
            for i in range(n):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
        return arr
                
                    
                
            
            
                
                