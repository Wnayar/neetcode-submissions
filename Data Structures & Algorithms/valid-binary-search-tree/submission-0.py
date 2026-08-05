# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l , r):
            # base case 
            if node is None:
                return True 
            
            # recursion checking valid range 
            if node.val > l and node.val < r:
                return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
            else:
                return False  
        
        return dfs(root, float('-inf') , float('inf'))