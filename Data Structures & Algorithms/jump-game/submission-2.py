from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        moving_end_index = len(nums) - 1

        if moving_end_index == 0:
            return True

        # start at second last index 
        for i in range(len(nums) - 2, -1, -1):
            if moving_end_index - i <= nums[i]:
                moving_end_index = i
            else:
                continue

        if moving_end_index == 0:
            return True
        else:
            return False

        
        