class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # intialize a heap of size k
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add to heap and pop smallest
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # return k largest which would be smallest in the min heap 
        return self.minHeap[0]
