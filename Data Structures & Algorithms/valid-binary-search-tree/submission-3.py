# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # time complexity: O(n)
        # # space complexity: O(h), where h is height of the binary tree (the longest recursive stack)
        # def dfs(node, l , r):
        #     # base case 
        #     if node is None:
        #         return True 
            
        #     # recursion checking valid range 
        #     if node.val > l and node.val < r:
        #         return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
        #     else:
        #         return False  
        
        # return dfs(root, float('-inf') , float('inf'))
        
        # time complexity: O(n)
        # space complexity; O(w), where w is the largets width of the tree at some given level 
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue: 
            node, l , r = queue.popleft()
            if node is None:
                continue 
            
            # check when not in range 
            if node.val <= l or node.val >= r:
                return False 

            # add to queue 
            queue.append((node.left, l, node.val))
            queue.append((node.right, node.val, r))

        return True  
