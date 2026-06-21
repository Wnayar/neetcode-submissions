from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy choice highest frequency goes next so long not on cool down
        
        # implement a max heap with frequnecies of letters
        # implement empty queue 
        freq_dict = Counter(tasks)
        max_heap = freq_dict.values()
        max_heap = [-i for i in max_heap]
        heapq.heapify(max_heap)
        time = 0
        queue = deque()
        cooldown = n + 1
        
        # pop max element, increment time per pop
        # reduce that max element by 1
        # add to a queue that max element - 1, (freq, time it was placed + cooldown)
        # on every loop check if can add back from queue to the max heap
        # terminate when queue and max heap is empty 
        while max_heap or queue:
            time += 1
            # greedy choice so must add back first 
            if queue:
                if queue[0][1] == time:
                    freq, _ = queue.popleft()
                    heapq.heappush(max_heap, -freq)
            if max_heap:
                freq = -heapq.heappop(max_heap)
                new_freq = freq - 1
                next_time = time + cooldown
                if new_freq > 0:
                    queue.append((new_freq, next_time))

        # return time 
        return time