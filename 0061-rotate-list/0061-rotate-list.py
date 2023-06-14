# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head 
        
        tail = head
        l = 1
        while tail.next:
            tail = tail.next
            l += 1
        # print(tail, l)
        tail.next = head
        t = l - k % l
        for i in range(t):
            tail = tail.next
    
        ans = tail.next
        tail.next = None
        return ans