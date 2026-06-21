# from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        # @cache
        cache  = {}
        def dp(i : int):
            index = i
            # base case 
            if index < 0:
                return 0
            
            # check cache 
            if i in cache:
                return cache[i]
            
            # recursion 
            result =  max(nums[index] + dp(index - 2) , dp(index -1))   

            # add to cache
            cache[i] = result  

            # recursion 
            return result 


        return dp(len(nums) - 1)
