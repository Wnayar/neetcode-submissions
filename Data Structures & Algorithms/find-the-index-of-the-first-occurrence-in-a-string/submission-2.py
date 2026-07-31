class Solution:
    # time compelxity: O(H * N), slicing is lineear, comapring is linear
    # space comepxlity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        lenH = len(haystack)
        lenN = len(needle)
        
        if lenN > lenH:
            return -1

        for i in range(lenH):
            if i + lenN > lenH:
                break
            if haystack[i : i + lenN] == needle:
                return i
        
        return -1