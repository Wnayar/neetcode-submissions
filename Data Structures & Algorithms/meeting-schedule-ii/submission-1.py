"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
# tc: O(nlogn) sorting and n * logn for insert operation  / popping heap, note heapify is just O(n) 
# sc: n  sorting in python is n timsort, heap also n
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # return early if empty
        if len(intervals) == 0:
            return 0

        # sort by starting times 
        intervals.sort(key = lambda x: x.start)
        # mantain a heap for ending times still in play 
        heap = []
        heapq.heappush(heap, intervals[0].end)
        # mantain a count for min number of rooms in use so far  
        count = 1 

        # iterate the intervals, greedily 
        for interval in intervals[1:]:
            if interval.start < heap[0]:
                count += 1
            else:
                heapq.heappop(heap)
            # update heap 
            heapq.heappush(heap, interval.end)

        return count    