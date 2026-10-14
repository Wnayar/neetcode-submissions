class Solution:
    # tc: O(n*m)
    # sc: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        rowZero = False 

        # mark col and rows which are to be zero using first row, first col and rowZero var 
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                # set col indicator as zero 
                    matrix[0][c] = 0
                # set row indicator as zero
                    if r == 0:
                        rowZero = True
                    else: 
                        matrix[r][0] = 0
        
        # set cols and rows to zero for inside  
        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 

        # set first col to zero if needed 
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0 

        # set first row to zero if needed 
        if rowZero == True:
            for c in range(col):
                matrix[0][c] = 0



        
        