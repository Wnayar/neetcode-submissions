from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        coln = len(grid[0])
        fresh_start = 0 
        rotten = 0
        q = deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0
        rotten = 0

        # get rotten starting pos and number of fresh 
        for r in range(row):
            for c in range(coln):
                if grid[r][c] == 2:
                    q.append((r, c))
                    rotten += 1

                if grid[r][c] == 1:
                    fresh_start += 1

        rotten_desired_total = fresh_start + rotten
        rotten = 0

        # multi step BFS, increment time
        while q:
            flag = False 
            cur_length_q = len(q)
            # do multiple BFS as one step 
            for _ in range(cur_length_q):
                r, c = q.popleft()
                # increment rotten counter if visited
                rotten += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= row or
                        nc < 0 or nc >= coln or
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue 
                    # valid expansion of bfs 
                    q.append((nr, nc))
                    # mark as seen immeditaely so others wont add it also 
                    grid[nr][nc] = 2
                    flag = True 
            if flag:
                time += 1
             
        # if rotten same as intial fresh return res else return -1
        if rotten == rotten_desired_total:
            return time
        else:
            return -1


        
        

