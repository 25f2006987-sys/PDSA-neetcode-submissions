# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev=None
        curr=head
        list1=[]
        if head==None:
            return False
        while curr.next!=None:
            if curr in list1:
                return True 
            list1.append(curr)
            curr=curr.next
        return False
        