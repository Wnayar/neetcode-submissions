class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        last_index = len(nums) - 1
        def dp(i: int, last: bool) -> int:
            if i < 0:
                return 0
            if i == 0:
                if last == True:
                    return 0
                else:
                    return nums[i]
            
            # check cache 
            if (i, last) in cache:
                return cache.get((i, last))

            if i == last_index:
                result = max(nums[i] + dp(i - 2, True), dp(i -1, last))   
            else:               
                result = max(nums[i] + dp(i - 2, last), dp(i -1, last))

            # add to cache 
            cache[(i, last)] = result

            return result
        
        return dp(len(nums) - 1, False)