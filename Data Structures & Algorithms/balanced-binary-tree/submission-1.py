# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        # dfs height no more than 1 of max 
        def dfs(root: Optional[TreeNode]) -> int:
            # base case
            if root is None:
                return 0
            
            # recursion 
            max_height_left = dfs(root.left)
            max_height_right = dfs(root.right)

            if abs(max_height_left - max_height_right) > 1:
                self.balance = False
                raise Exception("Not Balance")
            
            # logic 
            return 1 + max(max_height_left, max_height_right)
        
        try:
            dfs(root)
            return self.balance
        except: 
            return self.balance