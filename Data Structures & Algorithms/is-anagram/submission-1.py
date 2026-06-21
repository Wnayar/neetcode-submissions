class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create dict for s, key is letter, value is count 
        # for each letter in t, check if exist in s if not return false, if in decrment count 
        # at end check all values in dict if any is non zero return false, else true 
        s_list = list(s)
        s_dict = {}
        for i in s_list:
            if s_dict.get(i) != None:
                s_dict[i] = s_dict.get(i) + 1
            else:
                s_dict[i] = 1 

        t_list = list(t)
        for j in t_list:
            if s_dict.get(j):
                s_dict[j] = s_dict.get(j) - 1
            else:
                return False  

        for k in s_dict:
            if s_dict.get(k) != 0:
                return False

        return True