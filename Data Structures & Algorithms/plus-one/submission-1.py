class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #O(n) time, O(1) space for most, but if require bigger array O(n) space
        # for in range(start, stop - stops one before inclusive, step)
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits 

            digits[i] = 0

        return [1] + digits 

