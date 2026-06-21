# from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        cache = {}
        def dp(n:int):
            # base case
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            # check cache 
            if cache.get(n):
                return cache[n]

            # recursion
            result = dp(n - 1) + dp(n - 2)

            # add to ache 
            cache[n] = result

            return result

        return dp(n)