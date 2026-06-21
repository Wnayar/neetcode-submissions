class Solution:
    def reverseBits(self, n: int) -> int:
        # need 032b, if dotn have 0 it uses spaces, gives string
        nBitForm = format(n, "032b")
        # res = ""
        # for i in range(len(nBitForm) - 1, -1, -1):
        #     res += nBitForm[i]

        res = nBitForm[::-1]
        return int(res, 2)
        