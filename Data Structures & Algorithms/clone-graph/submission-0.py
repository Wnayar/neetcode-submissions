"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case if no nodes 
        if node == None:
            return None
        # map old nodes to new nodes, so wont recreate
        oldToNew = {}

        def dfs(node):
            # base case 
            if node in oldToNew:
                return oldToNew[node]

            # recursion
            copy = Node(node.val)
            # add to dict 
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # return copy because append needs it if not already made, also so u return root

            return copy
        return dfs(node)
        