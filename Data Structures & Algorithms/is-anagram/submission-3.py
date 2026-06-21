class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_l = list(s)
        s_l.sort()
        t_l = list(t)
        t_l.sort()
        if len(s_l) != len(t_l):
            return False 

        for i,j in zip(s_l, t_l):
            if i != j:
                return False

        return True