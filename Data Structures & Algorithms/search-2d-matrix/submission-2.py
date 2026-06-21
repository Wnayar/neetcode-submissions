class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row binary search
        l, r = 0, len(matrix) - 1
        n = len(matrix[0]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[m][0] < target and matrix[m][n] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] <= target and matrix[m][n] >= target:
                break
        

        row = m 

        # find coln binary search
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True    
        
        return False     
                