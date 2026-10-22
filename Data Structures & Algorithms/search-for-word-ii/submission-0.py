# make a trie class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie 
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        # dfs + backtracking
        def dfs(r, c, parent):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in parent.children):
                return 
            
            char = board[r][c]
            node = parent.children[char]

            # found word 
            if node.word is not None:
                res.append(node.word)
                node.word = None
            
            # mark cell as visited 
            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # backtrack
            board[r][c] = char 

            # prune unnecessary Trie Node, i.e useless nodes no children and not end of word 
            if not node.children and node.word is None:
                del parent.children[char]


        # call dfs on every cell 
        for r in range(ROWS):
            for c in range(COLS):
                if not root.children:
                    return res 
                dfs(r, c, root)
        
        return res 
        