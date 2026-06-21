from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        end_index = len(cost)
        @cache
        def dp(i: int) -> int:
            # base case
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1] 
            
            # recursion 1 or 2 steps back 
            if i == end_index:
                cur_cost = 0
            else: 
                cur_cost = cost[i]
            return min(cur_cost + dp(i - 1), cur_cost + dp(i - 2))
        
        return dp(end_index)

