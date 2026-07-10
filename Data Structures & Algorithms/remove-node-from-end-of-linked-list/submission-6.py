# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # the bonus to this question was doin in one pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        dummy = ListNode(0, head)
        l, r = dummy, dummy 

        # can do till n + 1 if u want while loop to terminate while right, defensive so no .next on null and left will end on correct spot 
        for i in range(n):
            r = r.next

        while r.next is not None:
            l = l.next 
            r = r.next

        l.next = l.next.next 

        return dummy.next

        