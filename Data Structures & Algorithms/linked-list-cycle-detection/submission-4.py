# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(N) time, O(1) space, Floyd Tortoise & Hare 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
        
        
        # O(N) time, O(N) space 
        # hashset = set()
        # while head:
        #     if head in hashset:
        #         return True
        #     hashset.add(head)    
        #     head = head.next

        # return False