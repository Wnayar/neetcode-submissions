# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            # base case 
            if root.left == None and root.right == None:
                res.append(root.val)
                return 
            
            if root.left:
                dfs(root.left)

            res.append(root.val)

            if root.right:
                dfs(root.right)
        
        if root == None:
            return res
        dfs(root)
        return res
        