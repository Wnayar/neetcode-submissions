class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define bounds 
        l, r = 1, max(piles)
        last_valid_k = -1
        while l <= r: 
            m = l + ((r - l) // 2)
            if self.can(piles, m, h):
                last_valid_k = m
                r = m - 1
            else:
                l = m + 1
        
        return last_valid_k

    def can(self, piles: List[int], k: int, h: int) -> int:
        # check if k valid 
        a = 0
        for i in piles:
            a += math.ceil(i / k)
        return a <= h










