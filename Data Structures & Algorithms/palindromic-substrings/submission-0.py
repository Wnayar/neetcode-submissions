class Solution:
    # tc: O(n^2)
    # sc: O(1)
    def countSubstrings(self, s: str) -> int:
        # intialize res for count of palindromes
        res = 0 

        # track odd length palindromes
        for i in range(len(s)):
            l, r = i, i 
            # check valid index and if palindrome 
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # track even length plaindromes 
        for i in range(len(s)):
            l, r = i, i + 1 
            # check if palindrome and valid index 
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # return res 
        return res

        