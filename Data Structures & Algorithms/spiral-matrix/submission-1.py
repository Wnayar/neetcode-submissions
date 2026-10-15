class Solution:
    # tc: O(nm)
    # sc: O(1) excluding output space
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # matrix[0] is okay as constraint says non empty
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []

        # the intuition is that l,r,t,b define the matrix space, impossible to have a matrix if this condtion violates 
        while l <= r and t <= b:
            # move right
            for i in range(l, r + 1):
                res.append(matrix[t][i]) 
            t += 1

            # move down 
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            # move left 
            # this if is for nasty edge case when its one row (eventually), if u dont have u get duplicated elements can trace to see
            if not t > b:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1

            # move up
            # this if is for nasty edge case when its one coln (eventually), if u dont have u get duplicated elements can trace to see
            if not r < l:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res 