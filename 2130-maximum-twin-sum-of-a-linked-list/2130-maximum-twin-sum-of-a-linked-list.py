# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left, right = 0, len(arr) - 1
        maxx = 0
        while left < right:
            maxx = max(arr[left]+arr[right], maxx)
            left += 1
            right -= 1
        return maxx