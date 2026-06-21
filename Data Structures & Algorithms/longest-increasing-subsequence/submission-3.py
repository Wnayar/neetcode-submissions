from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # dp(i) means longest subsequence if i was last value included
        @cache 
        def dp(i: int) -> int:
            # base case
            if i == 0:
                return 1

            # recursion 
            temp = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp, 1 + dp(j))
            return temp



        res = 1
        for i in range(n):
            res = max(res, dp(i))
        return res
