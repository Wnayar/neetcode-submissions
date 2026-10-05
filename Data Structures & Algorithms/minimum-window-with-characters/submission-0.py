class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case if t is empty
        if t == "":
            return ""

        have_count, need_count = 0, 0 
        have, need = {}, {}
        min_len = float('inf')
        res_index = [0, 0]
        l = 0

        # populate need dict and get conditon length 
        for c in t:
            need[c] = 1 + need.get(c, 0)
        need_count = len(need)

        # sliding window on s
        for r in range(len(s)):
            # add char to have dict if is in need dict 
            if s[r] in need:
                have[s[r]] = 1 + have.get(s[r], 0)
                # if this char count matches the count in need dict, increment condition count 
                if have[s[r]] == need[s[r]]:
                    have_count += 1

            # if have count matches need count, all condition met, increment L pointer and update length/ pointers
            if have_count == need_count:
                while have_count == need_count:
                    # record min length and indexes 
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        res_index = [l, r]
                    # remove oldest left value 
                    if s[l] in have:
                        have[s[l]] -= 1
                        # check if condition no longer still valid 
                        if not have[s[l]] >= need[s[l]]:
                            have_count -= 1
                    l += 1

        # if not found 
        if min_len == float('inf'):
            return ""

        # return sliced string based on res_index
        l, r = res_index
        return s[l: r + 1]


