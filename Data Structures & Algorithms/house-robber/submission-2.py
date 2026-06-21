from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dp(i : int):
            index = i
            # base case 
            if index < 0:
                return 0 

            # recursion 
            return max(nums[index] + dp(index - 2) , dp(index -1))

        return dp(len(nums) - 1)
