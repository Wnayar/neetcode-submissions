class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_d = defaultdict(set)
        c_d = defaultdict(set)
        b_d = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue 
                if v in r_d[r] or v in c_d[c] or v in b_d[(r // 3, c // 3)]:
                    return False 
                r_d[r].add(v)
                c_d[c].add(v)
                b_d[(r // 3, c // 3)].add(v)
        
        return True 

        