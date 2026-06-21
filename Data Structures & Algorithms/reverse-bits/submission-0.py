class Solution:
    def reverseBits(self, n: int) -> int:
        nBitForm = format(n, "032b")
        res = ""
        for i in range(len(nBitForm) - 1, -1, -1):
            res += nBitForm[i]

        return int(res, 2)
        