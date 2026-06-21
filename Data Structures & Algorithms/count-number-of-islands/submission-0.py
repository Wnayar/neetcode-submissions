from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Overview: O(n) multiple BFS

        # intialize a count variable to count islands 
        # intialize a seen set 
        res = 0
        
        # Double for loop to check every cell
        # Mark with seen if is 0 and continuy
        # For every cell if starts with 1 do bfs cardinal movement
        # Mark with seen if was in the bfs
        # in here when the bfs is done (only if bfs is done) meanigng #1 of 1, incrment count
        row = len(grid)
        col = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen_set = set()
        for r in range(row):
            for c in range(col):
                # if already in seen meaning bfs epxlored island or 0 then skip 
                if (c, r) in seen_set:
                    continue
                # add to seen 
                seen_set.add((c, r))
                if grid[r][c] == "0":
                    continue
                # starts with 1, can increae count by 1 for this whole new bfs 
                res += 1
                # make a queue for bfs and intialize 
                q = deque()
                q.append([c, r])
                # do bfs and add to see 
                while q:
                    x, y = q.popleft()
                    seen_set.add((x, y))
                    for nx, ny in directions:
                        next_x = x + nx 
                        next_y = y + ny
                        if (next_x < 0 or next_x >= col or 
                            next_y < 0 or next_y >= row):
                            continue
                        if grid[next_y][next_x] != "1":
                                continue 
                        # valid moves to another 1 
                        if (next_x, next_y) not in seen_set:
                            q.append([next_x, next_y])

        # return count
        return res 
