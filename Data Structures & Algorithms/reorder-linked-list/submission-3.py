# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time compelxity O(n), space complexity O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ealry terminates 
        if head is None or head.next is None:
            return      

        # (fast slow pointers) get middle (slow ends at end of first half)
        slow, fast = head, head 
        # note can do the varaint with fast 1 head of slow at start works also
        # it doesnt matter how but all u want is even n/2 each side, odd (n+1)/2 on the first side 
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None #split into first hald and secodn half        

        # (reverse list) second half  
        prev = None
        cur = second 
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        # merge two halves alternately  
        l, r = head, prev

        while l is not None and r is not None:
        # or can just check r is not None cause if u map out odd and even r case always none
            tmp_1 = l.next
            tmp_2 = r.next
            l.next = r
            r.next = tmp_1
            l = tmp_1
            r = tmp_2
        




        

