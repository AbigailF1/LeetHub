# Definition for singly-linked list.
class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead=ListNode()
        head1=list1
        head2=list2
        start=newhead
        while head1 and head2:
            node=ListNode()
            if head1.val<head2.val:
                node.val=head1.val
                head1=head1.next
            else:
                node.val=head2.val
                head2=head2.next
            newhead.next=node
            newhead=node
        if head1:
            newhead.next=head1
        else:
            newhead.next=head2
        return start.next

            
        
                
        
        
        