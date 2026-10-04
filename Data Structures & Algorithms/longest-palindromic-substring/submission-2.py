class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        min_l, max_r = 0, 0 

        for i in range(len(s)):
            # case 1: longest palindrome is odd 
            # assume i is the current centre 
            l, r = i, i 
            while l - 1 >= 0 and r + 1 <= len(s) - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            if r - l + 1 >= max_len:
                min_l = l
                max_r = r
                max_len = r - l + 1

            # case 2: longest palindrom is even 
            # assume i and i + 1 is the current centre
            l, r = i, i + 1 
            if r <= len(s) - 1 and s[l] == s[r]:
                while l - 1 >= 0 and r + 1 <= len(s) - 1 and s[l - 1] == s[r + 1]:
                    l -= 1
                    r += 1

                if r - l + 1 >= max_len:
                    min_l = l
                    max_r = r
                    max_len = r - l + 1
        
        return s[min_l: max_r + 1]
         