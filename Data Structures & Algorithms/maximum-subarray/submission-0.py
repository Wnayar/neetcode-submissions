class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dont include negative prefixes as it cant help, track max and build along the way 
        cur_max = nums[0]
        cur_prefix = 0

        for i in range(len(nums)):
            if cur_prefix < 0:
                cur_prefix = 0
            cur_prefix = cur_prefix + nums[i]
            cur_max = max(cur_max, cur_prefix)

        return cur_max



