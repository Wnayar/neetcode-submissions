class Solution:
    def isHappy(self, n: int) -> bool:
        n_s = str(n)
        hashset = set()
        while True:
            accum = 0
            for i in n_s:
                accum = accum + (int(i) * int(i))
                
            if accum == 1:
                return True
            if accum in hashset:
                return False

            hashset.add(accum)
            n_s = str(accum)