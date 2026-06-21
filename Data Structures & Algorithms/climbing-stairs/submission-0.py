from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(n:int):
            # base case
            if n == 0:
                return 1
            if n < 0:
                return 0

            # recursion
            return dp(n - 1) + dp(n - 2)

        return dp(n)