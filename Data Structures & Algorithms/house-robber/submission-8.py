# good dp question check previous submissions
# this is O(n) time and O(1) space bottom up 
# top down + memo is O(n) time and O(n) space
# you can convert top down to bottom upin O(n) space then later reduce to O(1) if trivial i.e using few state reliance
class Solution:
    def rob(self, nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            prev2 = nums[0]
            prev1 = max(nums[1], nums[0])

            # dp[0...len(nums) - 1]
            for i in range(2, len(nums)):
                curr = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return prev1


