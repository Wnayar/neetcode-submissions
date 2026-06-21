class Solution:
    def reverseBits(self, n: int) -> int:
        # # need 032b, if dotn have 0 it uses spaces, gives string
        # nBitForm = format(n, "032b")
        # # res = ""
        # # for i in range(len(nBitForm) - 1, -1, -1):
        # #     res += nBitForm[i]

        # res = nBitForm[::-1]
        # return int(res, 2)
        
        res = 0
        for i in range(32):
            # python right aligns, thus is like 0000..1
            bit = n & 1
            n = n >> 1
            res = res << 1
            res = res | bit
        return res 