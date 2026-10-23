class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. create a graph with every char 
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()

        # 2. build edges from adjacent words 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # invalid prefix case 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # find first difference 
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # 3. DFS with cycle detection (to find impossible)
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True # currently exploring 

            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False # finished exploring 
            res.append(c)
            return False 
            


        # 4. call DFS on all components as may be disconnected graph 
        for c in adj:
            if dfs(c):
                return ""

        # 5. reverse postorder 
        res.reverse()
        return "".join(res) 
