# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!=None:
            count+=1        
            curr=curr.next
        pos=count-n+1
        if pos==1:
            return head.next
        count=1
        curr=head
        
        while count<pos-1:
            curr=curr.next
            count+=1
        if curr.next!=None:
            curr.next=curr.next.next
        
        return head