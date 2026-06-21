class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def subSearch(index: int, cur: TrieNode) -> bool:
            for i, c in enumerate(word[index:]):
                if c == ".":
                    # wildcard explore all 
                    for key in cur.children:
                        if subSearch(index + i + 1, cur.children[key]):
                            return True
                    return False
                elif c not in cur.children:
                    return False
                cur = cur.children[c]

            return cur.endOfWord 
        
        return subSearch(0, cur)     
