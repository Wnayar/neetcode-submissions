# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # slow and fast pointers 
        s, f  = head, head 
        prev = None

        # get to end of first half, and start of secodn half. First half gets reversed while doing this 
        while f.next.next is not None:
            # fast pointer update by 2, fast must be moved first because f and s poiitnign to same node at start and if u reverse first without update fast u go into none  
            f = f.next.next 

            # reverse 
            nxt = s.next 
            s.next = prev
            prev = s

            # slow pointer update by one
            s = nxt 

        # reset f to be start of second half 
        f = s.next 
        # make s reverse last, if you draw out will see s has not reverse last 
        s.next = prev

        # s is at end of first half and first half has been reversed, f is at start of second half
        res = 0
        while True:
            res = max(res, s.val + f.val)
            # progress f exit if none
            f = f.next
            if f == None:
                break
 
            s = s.next  
        
        return res 
