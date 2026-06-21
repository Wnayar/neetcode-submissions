class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n + 1):
            temp_ones = 0

            for j in format(i, 'b'):
                if j == '1':
                    temp_ones += 1
            
            res.append(temp_ones)
        
        return res
        