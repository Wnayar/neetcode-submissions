from functools import cache 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can only move down or right, since starting from end is up and left
        dr = [(-1, 0), (0, -1)]
        row = m - 1
        coln = n - 1

        @cache
        def dp(m, n):
            # base case start point 
            if m == 0 and n == 0:
                return 1

            # recursion 
            accum = 0
            for dm, dn in dr:
                nm = m + dm
                nn = n + dn
                if (nm < 0 or nm > row or
                    nn < 0 or nn > coln):
                    continue 
                # valid moves 
                accum += dp(nm, nn)

            return accum

        return dp(row, coln)
        