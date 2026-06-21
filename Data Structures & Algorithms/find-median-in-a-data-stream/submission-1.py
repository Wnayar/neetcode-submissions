# Time complexity: addNum O(logn), findMedian O(1)
class MedianFinder:

    def __init__(self):
        # two heaps, self.LHS max heap, self.RHS is a min Heap
        self.LHS = []
        self.RHS = []
        
    def addNum(self, num: int) -> None:
        # add to the self.LHS heap
        # check if self.LHS heap max is more than self.RHS min, move over 
        # always want to ensure |self.LHS| is no more than 1 |self.RHS|
        heapq.heappush(self.LHS, -num)

        if self.RHS:
            if -self.LHS[0] > self.RHS[0]:
                val = -heapq.heappop(self.LHS)
                heapq.heappush(self.RHS, val)
        
        # ensure LHS is at most more than 1 RHS
        if len(self.LHS) > len(self.RHS) + 1:
            val = -heapq.heappop(self.LHS)
            heapq.heappush(self.RHS, val)        

        if len(self.RHS) > len(self.LHS):
            val = -heapq.heappop(self.RHS)
            heapq.heappush(self.LHS, val)       

    
    def findMedian(self) -> float:
        length = len(self.LHS) + len(self.RHS)
        # if even then max self.LHS, and min self.RHS average 
        if length % 2 == 0:
            return (-self.LHS[0] + self.RHS[0]) / 2

        # if odd then max self.LHS
        return float(-self.LHS[0])
        
        