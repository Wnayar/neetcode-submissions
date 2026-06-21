class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        coln = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        length = len(word)
        seen = set()

        def dfs(r, c, i):
            seen.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if i == length -1 and board[r][c] == word[i]:
                    return True 
                if (nr < 0 or nr >= row or
                    nc < 0 or nc >= coln or 
                    i >= length or
                    board[nr][nc] != word[i + 1] or 
                    (nr, nc) in seen):
                    continue
                # valid expansion
                if dfs(nr, nc, i + 1):
                    return True
            seen.remove((r, c))
            return False 


        for r in range(row):
            for c in range(coln):
                if board[r][c] != word[0]:
                    continue
                # valid start
                res = dfs(r, c, 0)
                if res:
                    return True

        return False
        