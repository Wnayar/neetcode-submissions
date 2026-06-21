# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # time complexity is O(n) visit every node, space O(n) worst case one long chain recursive stack
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def dfs(root: Optional[TreeNode]) -> tuple(int, bool):
            # base case
            if root is None:
                return (0, True)
            
            # recursion 
            left_call = dfs(root.left)
            right_call = dfs(root.right)

            max_height_left = left_call[0]
            left_bool = left_call[1]
            max_height_right= right_call[0]
            right_bool = right_call[1]

            if abs(max_height_left - max_height_right) > 1:
                return (1 + max(max_height_left, max_height_right), False and left_bool and right_bool)
            
            # logic 
            return (1 + max(max_height_left, max_height_right), True and left_bool and right_bool)

        return dfs(root)[1]




    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     self.balance = True
    #     # dfs height no more than 1 of max 
    #     def dfs(root: Optional[TreeNode]) -> int:
    #         # base case
    #         if root is None:
    #             return 0
            
    #         # recursion 
    #         max_height_left = dfs(root.left)
    #         max_height_right = dfs(root.right)

    #         if abs(max_height_left - max_height_right) > 1:
    #             self.balance = False
    #             raise Exception("Not Balance")
            
    #         # logic 
    #         return 1 + max(max_height_left, max_height_right)
        
    #     try:
    #         dfs(root)
    #         return self.balance
    #     except: 
    #         return self.balance