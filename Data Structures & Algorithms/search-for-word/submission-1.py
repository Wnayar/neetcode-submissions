class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # base case 1: invalid move -> out of bounds, alrdy visited, does not match word 
            if (r >= row or r < 0 or 
                c >= col or c < 0 or
                (r, c) in path or 
                board[r][c] != word[i]
                ):
                return False 
            # base case 2: word if found 
            if i == len(word) - 1:
                return True

            # recursion 
            path.add((r, c))
            have = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return have 

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0) == True:
                    return True
        
        return False 

        