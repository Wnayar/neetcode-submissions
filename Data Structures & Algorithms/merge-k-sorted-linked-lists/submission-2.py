import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # populate our heap 
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        cur = ListNode(0, None)
        dummy = cur

        # build sorted link list 
        while heap:
            _, i, cur.next = heapq.heappop(heap)
            nxt = cur.next.next
            if nxt:
                heapq.heappush(heap, (nxt.val, i, nxt))
            cur = cur.next

        return dummy.next

