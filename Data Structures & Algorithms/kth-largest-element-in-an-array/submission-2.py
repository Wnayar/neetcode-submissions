class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make max heap  O(n)
        numsTemp = [-i for i in nums]
        heapq.heapify(numsTemp)

        # pop from the max heap k times and return last k pop O(klogn)
        res = -1001
        for j in range(k):
            res = -heapq.heappop(numsTemp)

        return res