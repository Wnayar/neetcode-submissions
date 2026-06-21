from functools import cache
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            n = n - 3
            return dp(n) + dp(n + 1) + dp(n + 2)
        
        return dp(n)
        