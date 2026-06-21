from functools import cache 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1_n = len(text1) - 1
        t2_n = len(text2) - 1

        @cache
        def dp(t1_n, t2_n):
            # base case 
            if t1_n == -1 or t2_n == -1:
                return 0

            # recursion max 
            res = 0
            # case 1 if both are the same include 
            if text1[t1_n] == text2[t2_n]:
                res = max(res, 1 + dp(t1_n - 1, t2_n - 1))
            # case 2 if they are different explore both path keep one discard one go both way 
            else:
                res = max(res, dp(t1_n - 1, t2_n), dp(t1_n, t2_n - 1))
            return res
            
        return dp(t1_n, t2_n)