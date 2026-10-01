# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val : i for i, val in enumerate(inorder)}
        # track current index in preorder list
        pre_idx = 0

        # l and r are the boundries of current subtree in inorder list
        def recurse(l, r):
            # base case no more elements 
            if l > r:
                return  

            # recursion
            nonlocal pre_idx
            root = TreeNode(preorder[pre_idx])
            # increment pre index by 1 because dfs, naturally correct position 
            pre_idx += 1
            mid = index[root.val]

            root.left = recurse(l, mid - 1)
            root.right = recurse(mid + 1, r)

            return root

        return recurse(0, len(inorder) - 1)