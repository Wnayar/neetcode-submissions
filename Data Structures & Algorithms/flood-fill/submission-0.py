class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # bfs and change colour in cardinal movement
        q = deque()
        q.append([sr, sc])
        original_color = image[sr][sc]

        # if src is same as color, then no changes, as changign thos esame pixel as start 
        if image[sr][sc] == color:
            return image 
            
        # colour first one
        image[sr][sc] = color

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # if out of bounds continue 
                if (nr < 0 or nr == len(image) or
                    nc < 0 or nc == len(image[0])):
                    continue
                # if in bounds and same colour as original -> add to queue
                if image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append([nr, nc])

        return image
        