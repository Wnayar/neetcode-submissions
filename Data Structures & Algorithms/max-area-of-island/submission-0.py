class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        temp = 0
        dr = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            nonlocal temp
            # mark as seen and update temp area 
            grid[r][c] = 0
            temp += 1
            # if valid move continue dfs 
            for row, coln in dr:
                # invalid -> continue 
                nr = r + row
                nc = c + coln
                if (nr < 0 or nr >= len(grid) or
                    nc < 0 or nc >= len(grid[0]) or
                    grid[nr][nc] == 0):
                    continue
                dfs(nr, nc)
            return 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # reset temp to 0  
                temp = 0
                # calculate max temp via dfs, if valid start 
                if grid[i][j] == 1:
                    dfs(i, j)
                res = max(res, temp)
        
        return res 