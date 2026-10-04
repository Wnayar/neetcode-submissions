class Solution:
    # tc: O(n), like 52n at most l moves across once and r moves across once, each dic values is. 
    # there is a pure n solution but i just dont think its intuitive enough to leanr but its about
    # maintaing a max_f that is possible stale to try and avoid doign the dict.values() call
    # sc: O(1), 26 chars  
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = {}
        res = 0

        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)

            # dict.values returns an dict value which is an iterabel object thus max works, 
            # but certain array operations i.e indexing wont work
            if r - l + 1 - max(dic.values()) <= k:
                res = max(res, r - l + 1)
            else:
                while r - l + 1 - max(dic.values()) > k:
                    dic[s[l]] -= 1
                    l += 1
        
        return res 