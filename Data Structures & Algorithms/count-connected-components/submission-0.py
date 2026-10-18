class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adjacency list 
        adj = {i: [] for i in range(n)}
        for l, r in edges:
            adj[l].append(r)
            adj[r].append(l)
        
        # make a visited set 
        visited = set()

        # define a dfs 
        def dfs(cur):
            # base cases 
            if cur in visited:
                return
            neighbours = adj[cur]
            if not neighbours:
                return 

            # mark cur as visited 
            visited.add(cur)
            # recursion
            for nei in neighbours:
                dfs(nei)

        # track number of connected components 
        res = 0
        # for loop call the dfs
        for i in range(n):
            # if seen current element no need to revisit 
            if i in visited:
                continue
            dfs(i)
            # thus we just count number of dfs of elements first time we seeing
            res += 1 

        # return result 
        return res 