class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1

        def dp(i : int) -> bool:
            # base cases
            if i >= last_index:
                return True
            # if not at end and 0 jump at current position
            if nums[i] == 0:
                return False

            # recursion 
            res = False
            jumps = nums[i]
            for jump in range(1, nums[i] + 1):
                res = res or dp(i + jump)
            
            return res

        
        return dp(0)
        
        