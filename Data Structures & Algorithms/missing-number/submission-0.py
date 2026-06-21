class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        expectedSum = 0
        actualSum = 0
        for i in range(length + 1):
            expectedSum += i
        for j in nums:
            actualSum += j
        
        return expectedSum - actualSum