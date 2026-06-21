# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # call same tree at every node
    def isSubtree(self, root, subRoot) -> bool:
        # base case 
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False     

        # early prune (if doesnt rely on recursion)
        bool_current = self.sameTree(root, subRoot)
        if bool_current:
            return True

        # recursion 
        bool_left = self.isSubtree(root.left, subRoot)
        # can prune early if left side true already
        if bool_left:
            return True
        bool_right = self.isSubtree(root.right, subRoot)

        # logic
        return bool_left or bool_right

    # same tree
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        if root is None and subRoot is None:
            return True
        
        if root is not None and subRoot is None:
            return False 

        if root is None and subRoot is not None:
            return False

        # early prune
        sameTree_bool_current = root.val == subRoot.val
        if sameTree_bool_current is False:
            return False

        # recursion 
        sameTree_bool_left = self.sameTree(root.left, subRoot.left)
        sameTree_bool_right = self.sameTree(root.right, subRoot.right)   

        # logic     
        return sameTree_bool_current and sameTree_bool_left and sameTree_bool_right