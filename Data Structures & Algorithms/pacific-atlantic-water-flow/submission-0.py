class Solution:
    # tc: n * m where n is row, and m is column as just dfs with visted 
    # sc: n * m if all were acceptable
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        COL = len(heights[0])
        ROW = len(heights)
        pac, atl = set(), set()
        res = []

        def dfs(row, col, prevH, ocean):
            if (row >= ROW or col >= COL or
                row < 0 or col < 0 or
                heights[row][col] < prevH or 
                ((row, col) in ocean)) :
                return 

            ocean.add((row, col))

            # traverse cardinal directions NSWE
            dfs(row - 1, col, heights[row][col], ocean)
            dfs(row + 1, col, heights[row][col], ocean) 
            dfs(row, col - 1, heights[row][col], ocean)
            dfs(row, col + 1, heights[row][col], ocean)  

        for c in range(COL):
            dfs(0, c, heights[0][c], pac)
            dfs(ROW -1, c, heights[ROW -1][c], atl)
        
        for r in range(ROW):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COL -1, heights[r][COL -1], atl)       

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        
        return res