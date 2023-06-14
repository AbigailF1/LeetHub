# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next or not fast.next.next: return 
        
        new_slow = head
        while slow.next:
            if new_slow == slow: return slow
            slow = slow.next
            new_slow = new_slow.next
        return
            
        