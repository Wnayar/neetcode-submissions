class Solution:
    # time complexity O(n^2), space complexity O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for rows
        for r in board:
            r_d = set()
            for v in r:
                if v == ".":
                    continue 
                if v in r_d:
                    return False
                r_d.add(v)

        # check for colns
        for i in range(len(board[0])):
            c_d  = set()
            for r in board:
                if r[i] == ".":
                    continue 
                if r[i] in c_d:
                    return False 
                c_d.add(r[i])

        #check for sub-boxes
        r_t = 0
        c_t = 0
        for i in range(9):
            b_d = set()
            for r in range(3):
                for c in range(3):
                    if board[r + r_t][c + c_t] == ".":
                        continue
                    if board[r + r_t][c + c_t] in b_d:
                        return False 
                    b_d.add(board[r + r_t][c + c_t])
            c_t += 3
            if c_t == 9:
                c_t = 0
                r_t += 3
            

        return True