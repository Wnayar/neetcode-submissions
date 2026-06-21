from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amt: int) -> int:
            # base case
            if amt == 0:
                return 0
            if amt < 0:
                return 10001

            # recursion
            res = 10001
            for coin in coins:
                res = min(1 + dp(amt - coin), res)
            
            return res

        
        temp = dp(amount)
        if temp > 10000:
            return -1

        return temp

        