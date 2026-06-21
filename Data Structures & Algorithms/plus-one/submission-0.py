class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #O(n) time, O(1) space 
        last = len(digits) - 1
        while last >= 0:
            digits[last] = digits[last] + 1
            if digits[last] != 10:
                return digits
            else:
                digits[last] = 0
                last = last - 1
                if last == -1:
                    return [1] + digits
        
        return digits