class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m 

        # l or r + 1 must think of invaraints
        # everything before l is smaller than T -> l first valid
        # everything after r is bigger than T -> r + 1 first valid, becauseu keep r 
        return r + 1