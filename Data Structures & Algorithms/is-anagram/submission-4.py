class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_d, t_d = {}, {}
        
        if len(s) != len(t):
            return False

        for i, j in zip(s, t):
            s_d[i] =  s_d.get(i, 0) + 1
            t_d[j] =  t_d.get(j, 0) + 1
        
        for i in s_d:
            if s_d[i] != t_d.get(i, 0):
                return False 

        return True  

