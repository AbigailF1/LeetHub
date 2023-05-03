# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        head = ListNode()
        for i in range(len(lists)):
            if lists[i]:
                heappush(arr, [lists[i].val,i,lists[i]])
                lists[i] = lists[i].next
        #print(arr[0])
        
        head2 = head
        while arr:
            value, index , lists2 = heappop(arr)
            head2.next = ListNode(value)
            head2 = head2.next
            if lists2.next:
                heappush(arr, [lists2.next.val, index, lists2.next])
                # lists[i] = lists[i].next            
        
        return head.next
        