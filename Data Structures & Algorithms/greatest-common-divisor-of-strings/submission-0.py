class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        minLen = min(len1, len2)
        minStr = None

        if minLen == len1:
            minstr = str1
        else:
            minstr = str2

        def isDivisible(l: int) -> bool:
            # if not multiples return 
            if len1 % l != 0 or len2 % l != 0:
                return False 
            
            # if multiples then check if valid 
            f1 = len1 // l
            f2 = len2 // l
            str1New = f1 * minstr[:i]
            str2New = f2 * minstr[:i]
            if str1New != str1 or str2New != str2:
                return False 
            return True 

        for i in range(minLen, 0, -1):
            if isDivisible(i):
                return minstr[:i]
        
        return ""



        