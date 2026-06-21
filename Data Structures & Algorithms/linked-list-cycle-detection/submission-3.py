# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(N) time, O(1) space, Floyd Tortoise & Hare 
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next 
        while True:
            if fast is None or fast.next is None:
                return False
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        
        # O(N) time, O(N) space 
        # hashset = set()
        # while head:
        #     if head in hashset:
        #         return True
        #     hashset.add(head)    
        #     head = head.next

        # return False