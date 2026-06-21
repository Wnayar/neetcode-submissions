class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # length = len(nums)
        # expectedSum = 0
        # actualSum = 0
        # for i in range(length + 1):
        #     expectedSum += i
        # for j in nums:
        #     actualSum += j
        
        # return expectedSum - actualSum

        #xor is commutative a ^ b == b ^ a, and associative (a ^ b) ^ c === a ^ (b ^ c)
        # can write it out and xor with self is 0, a xor 0 is a 
        n = len(nums)
        res = 0
        for i in range(n):
            res = res ^ nums[i] ^ i
        res = res ^ n
        return res
