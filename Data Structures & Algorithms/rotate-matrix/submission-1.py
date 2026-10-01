class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose 
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                temp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = temp
        
        # reverse
        for r in matrix:
            r.reverse()


# 1 2 3
# 4 5 6
# 7 8 9 

