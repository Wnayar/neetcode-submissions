class Solution:
    # tc: O(n), sc: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        res = 0
        l, r = 0, 0

        for c in s:
            if c in cur:
                while c in cur:
                    cur.remove(s[l])
                    l += 1
            
            res = max(res, r - l + 1)
            r += 1
            cur.add(c)

        return res