# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new = ListNode()
        cur = head
        while cur:
            prev = new
            while prev.next and cur.val >= prev.next.val:
                prev = prev.next
            cur.next, prev.next,cur = prev.next, cur,cur.next
            
            
        return new.next
        