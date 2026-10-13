class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case if no nodes still considered a valid tree 
        if n == 0:
            return False 

        visited = set()

        # adjaceny list to improve lookup 
        adj = {i: [] for i in range(n)} 
        for bef, aft in edges:
            adj[bef].append(aft)
            adj[aft].append(bef)

        def dfs(prev, nxt):
            # cycle detected return false 
            if nxt in visited:
                return False 
            # add to seen set 
            visited.add(nxt)

            for node in adj[nxt]:
                # skip previous node to prevent false positive detection of cycles
                if node == prev:
                    continue 
                # on first False can return it 
                if not dfs(nxt, node):
                    return False 
            
            return True 
             
        
        # return True if no cycles and connected 
        return dfs(-1, 0) and len(visited) == n


