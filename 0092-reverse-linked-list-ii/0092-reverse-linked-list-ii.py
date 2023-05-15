# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_node = ListNode(0, head)
        
        left_node, cur = new_node , head
        l = left
        while l - 1:
            left_node = cur
            cur = cur.next
            l -= 1
        
        prev = None
        for i in range(right - left +1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        left_node.next.next = cur
        left_node.next = prev
        
        return new_node.next
        