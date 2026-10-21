class Solution:
    def numDecodings(self, s: str) -> int:
        # define a dp cache 
        dp = {}

        # define a recursive function, where i is current index  
        def recur(i):
            # check dp cache
            if i in dp:
                return dp[i]

            # base case: if sucessfully decode word where last decode is 1 number
            if i == len(s) - 1 and s[i] != "0":
                return 1
            # base case: if succesfulyl decode word where last decode is 2 numbers
            if i == len(s):
                return 1
            # base case: if impossible to decode starts with "0"
            if s[i] == "0":
                return 0 

            # recursion, exploring valid indexes
            res1, res2 = 0, 0
            if i + 1 <= len(s) - 1:
                res1 = recur(i + 1)
            if i + 1 <= len(s) - 1 and s[i] in "12":
                if s[i] == "2" and s[i + 1] in "0123456":
                    res2 = recur(i + 2)
                elif s[i] == "1":
                    res2 = recur(i + 2)

            # add to dp cache if not inside 
            dp[i] = res1 + res2

            return dp[i] 

        # call the recurison 
        return recur(0)
        