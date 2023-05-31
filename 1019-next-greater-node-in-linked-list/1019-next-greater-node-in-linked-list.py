# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        stack = [0]
        ans = [0] * len(arr)
        for i in range(1, len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                ans[stack[-1]] = arr[i]
                stack.pop()
            stack.append(i)
        return ans
                
            
            
        