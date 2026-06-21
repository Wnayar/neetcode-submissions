from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = (len(nums) // 2) + 1
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        for k, v in d.items():
            if v >= maj:
                return k