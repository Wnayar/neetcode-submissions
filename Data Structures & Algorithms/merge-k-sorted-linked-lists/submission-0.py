import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    # time complexity O(n.logk) as n elements looked at and each element is logk from the heap to pop/push, space comexplity O(k) as reusing all nodes and heap is size k 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # heap comaprison on tuples is lexicographic, (val, index form array, node). heap crashes if tie breaker is same
        # this works as when pop will replace only from own list, so cant have two elements from one list in heap 
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # if no heap dummry.next returns none, els edummy.next will get the head element discovered in while loop below 
        dummy = ListNode(0)
        cur = dummy     

        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node 
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next