class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashset = set()
        while True:
            accum = self.eqn(n)

            if accum == 1:
                return True
            if accum in hashset:
                return False

            hashset.add(accum)
            n = accum  

    def eqn(self, n: int) -> int:
        accum = 0
        while n > 0:
            accum += (n % 10) ** 2
            n = n // 10

        return accum