class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = format(n, 'b')
        res = 0
        for i in bin_str:
            if i == '1':
                res += 1
        return res