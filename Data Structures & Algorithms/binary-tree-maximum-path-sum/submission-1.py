# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # tc: O(n)
    # sc: O(h), height of tree from recursion calls
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(root):
            # base case 
            if root == None:
                return 0 

            # recursion     
            # no split 
            max_left = max(0, dfs(root.left))
            max_right = max(0, dfs(root.right))

            # split 
            res[0] = max(res[0], root.val + max_left + max_right)

            return root.val + max(max_left, max_right)
            

        dfs(root)
        return res[0]