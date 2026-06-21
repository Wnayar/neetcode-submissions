from collections import deque
# dfs solution 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs every point, increment count by 1, mark as seen 
        row = len(grid)
        coln = len(grid[0])
        count = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # conduct bfs on connected 1s, mark as seen by changing to 0
        def dfs(r, c):
            q = deque()
            # garuntee first instance is 1, safe to add
            q.append((r, c))
            grid[r][c] == "0"
            while q:
                cr, cc = q.pop()
                for dr, dc in moves:
                    nr = cr + dr
                    nc = cc + dc
                    if (nr < 0 or nr >= row or
                        nc < 0 or nc >= coln or
                        grid[nr][nc] == "0"):
                        continue
                    # valid 1 
                    q.append((nr, nc))
                    # marks as seen 
                    grid[nr][nc] = "0"

        for r in range(row):
            for c in range(coln):
                if grid[r][c] == "0":
                    continue 
                else:
                    # grid[r][c] == "1"
                    dfs(r, c)
                    count += 1
        
        return count