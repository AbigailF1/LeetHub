# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        wanted = head.next
        even = head.next
        
        while odd and even and odd.next and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd = odd.next
            even = even.next
        odd.next = wanted
        return head
        