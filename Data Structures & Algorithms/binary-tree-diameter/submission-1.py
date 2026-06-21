# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # instance var to track max diameter
        self.diameter = 0

        # dfs to find max height at any point
        def dfs(root:Optional[TreeNode]) -> int:
            # base case 
            if root is None:
                return 0
            
            # recursion 
            max_left_height = dfs(root.left)
            max_right_height = dfs(root.right)

            # update diameter 
            self.diameter = max(self.diameter, max_left_height + max_right_height)

            # logic
            return 1 + max(max_left_height, max_right_height)

        dfs(root)
        return self.diameter