# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        # go through once to get the total length 
        l = 0
        e = head
        while e != None:
            e = e.next
            l += 1
        
        # early termination
        if l == 1:
            return None 
        if l == n: # since no differenc below algo cant handle
            return head.next

        # get 3 adjacent nodes 
        count = 0
        prev, cur = None, head
        while count != l - n:
            prev = cur
            cur = cur.next 
            count += 1
        nxt = cur.next 

        # manage pointers 
        prev.next = nxt

        return head

        