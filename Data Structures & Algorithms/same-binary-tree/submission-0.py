# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #dfs but check values 
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # base case
            if p is None and q is None:
                return True
            
            if p is None and q is not None:
                return False

            if p is not None and q is None:
                return False
            
            # recursion
            bool_dfs_left = dfs(p.left, q.left)
            bool_dfs_right = dfs(p.right, q.right) 

            # logic 
            bool_current = p.val == q.val
            return bool_current and bool_dfs_left and bool_dfs_right

        return dfs(p,q)