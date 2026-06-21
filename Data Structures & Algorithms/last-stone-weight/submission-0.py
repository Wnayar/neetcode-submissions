class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make a max heap
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)

        # destroy till 1 or non remain 
        while len(max_heap) > 1:
            heaviest1 = -heapq.heappop(max_heap)
            heaviest2 = -heapq.heappop(max_heap)

            # if same destroy both (do nothing)

            # if not same heaviest1 - heaviest2 and add back
            if heaviest1 != heaviest2:
                afterSmash = heaviest1 - heaviest2
                heapq.heappush(max_heap, -afterSmash)

        # return weight of last stone or 0 if none
        # if max_heap empty just add back a 0 in case 
        heapq.heappush(max_heap, 0)
        return -max_heap[0]