class Solution:
    # tc: O(m*n*4^w), where m is rows, n is colns, and w is length of word. Could argue 3^w because cant revisit
    # Notes that 4 ^ w is number of leaves, is actually a GP series 1 + 4 + 16 .. +  4 ^ w 
    # if u solve u get ((4^ (w + 1)) - 1) / 3, and if u remove factors and break the 4 u left with 4 ^ w 
    # and the intuition is that the leaves dominate the tree anyway 
    # sc: O(w), w is length of word. Could argue min(w, m*n)
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

        