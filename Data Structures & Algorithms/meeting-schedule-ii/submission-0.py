"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

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
        # mantain a count for number of rooms in use 
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