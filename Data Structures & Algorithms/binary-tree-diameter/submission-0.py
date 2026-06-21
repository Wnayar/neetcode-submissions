# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.resDiameterMax = 0

        # dfs to track heigt, and update diamter
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            maxHeightLeft = dfs(root.left) 
            maxHeightRight = dfs(root.right)
            self.resDiameterMax = max(self.resDiameterMax, maxHeightLeft + maxHeightRight)

            return 1 + max(maxHeightLeft, maxHeightRight)
        
        dfs(root) 
        return self.resDiameterMax