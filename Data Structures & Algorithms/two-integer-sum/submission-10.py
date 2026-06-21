class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                h = {}

                # key to be num, value to be index
                for i, n in enumerate(nums):
                        diff = target - n
                        if diff in h:
                                return [h[diff], i]

                        h[n] = i 

