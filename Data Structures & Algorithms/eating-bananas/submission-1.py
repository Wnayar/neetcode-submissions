class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define bounds
        l, r = 1, max(piles)
        m = -1
        while l <= r:
            m = l + ((r - l) // 2)
            if self.can(piles, m, h):
                r = m - 1                
            else:
                l = m + 1

        return l
    
    def can(self, piles: List[int], k: int, h: int) -> bool:
        # check if k can 
        a = 0
        for i in piles: 
            a += math.ceil(i / k)
        return a <= h