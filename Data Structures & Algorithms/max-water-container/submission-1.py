class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        
        # move the pointer which is smaller in height
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            # check if l or r is smaller then advance that one
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else: 
                # if both same, u have max area for that height, so both will eb discarded eventually, so doesnt matetr which oen progress 
                l += 1
        
        return res 