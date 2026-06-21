class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        # binary search to find row
        row = None
        l, r = 0, m
        while l <= r:
            mid = l + ((r - l) // 2) 
            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if row == None:
            return False 

        # binary search to find coln
        l, r = 0, n
        while l <= r:
            mid = l + ((r - l) // 2) 
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True 
        
        return False