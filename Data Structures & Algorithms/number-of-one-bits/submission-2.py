class Solution:
    # time complexity O(1) because they say it will fit in 32 bits so max 32 loops i.e O(1), space complexity O(1)
    def hammingWeight(self, n: int) -> int:
        # n & 1 it will be for exampel 5 -> 101 and 001 => all zero except lsb which becomes 0 or 1, 1 if its 1
        res = 0
        while n != 0:
            if (n & 1) == 1:
                res += 1
            n =  n >> 1

        return res




        # bin_str = format(n, 'b')
        # res = 0
        # for i in bin_str:
        #     if i == '1':
        #         res += 1
        # return res