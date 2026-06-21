from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) - 1

        # dp(i) represents the current max and min ending at index i
        @cache
        def dp(i) -> Tuple[int, int]:
            # base case 
            if i == 0:
                return (nums[i], nums[i])
            # recursion
            prev_max, prev_min = dp(i - 1)
            cur_max_end_at_i = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            cur_min_end_at_i = min(nums[i], prev_max * nums[i], prev_min * nums[i])

            return cur_max_end_at_i, cur_min_end_at_i


        # populate the db, technially dont need this step as for loop below will do it
        #dp(n)

        # go through the dp to get the max 
        global_max = nums[0]
        for i in range(n + 1):
            max_ending_at_i, _ = dp(i)
            global_max = max(global_max, max_ending_at_i)
        return global_max


        