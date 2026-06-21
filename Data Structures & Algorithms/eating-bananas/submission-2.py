class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define bounds
        l, r = 1, max(piles)
        m = -1
        last_valid_can = -1
        while l <= r:
            m = l + ((r - l) // 2)
            if self.can(piles, m, h):
                last_valid_can = m
                r = m - 1                
            else:
                l = m + 1

        return last_valid_can
    
    def can(self, piles: List[int], k: int, h: int) -> bool:
        # check if k can 
        a = 0
        for i in piles: 
            a += math.ceil(i / k)
        return a <= h