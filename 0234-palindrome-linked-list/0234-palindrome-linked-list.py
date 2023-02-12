# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur=None
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            cur,cur.next,slow=slow,cur,slow.next
        if fast:
            slow=slow.next
        while slow and slow.val==cur.val:
            slow,cur=slow.next,cur.next
        return not slow