from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        INF = float('inf')

        @cache
        # at a given index what is the current longest increasing subseqeunce
        def dp(i: int, last_valid: int) -> int:
            # base case
            if i == 0:
                if nums[i] < last_valid:
                    return 1
                else:
                    return 0
            res = 0
            # recursion
            if nums[i] < last_valid:
                res = 1 + dp(i - 1, nums[i])

            return max(res, dp(i - 1, last_valid))


        return dp(last_index, INF)
        