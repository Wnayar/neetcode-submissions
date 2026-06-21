class Solution:
    # Time Complexity O(N), Space Complexity O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        d = 1
        pre= [0] * l
        post = [0] * l
        res = [0] * l

        # populate the prefix 
        for i in range(l):
            if i == 0:
                pre[i] = d
                continue 
            pre[i] = nums[i - 1] * pre[i - 1]
        
        # populate the postfix
        for j in range(l - 1, -1, -1):
            if j == l - 1:
                post[j] = d
                continue 
            post[j] = nums[j + 1] * post[j + 1]
            
        # populate the res array as product of prefix and postfix arrays at each index 
        for k in range(l):
            res[k] = pre[k] * post[k]

        return res 
        