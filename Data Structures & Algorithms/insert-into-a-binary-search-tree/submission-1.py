# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time complexity: O(h), where h is height of tree 
    # space complexity O(1), just tracking cur and creatine one new node
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        cur = root
        while True:
            if val < cur.val:
                if cur.left == None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left 
            else:
                if cur.right == None:
                    cur.right = TreeNode(val)
                    break               
                cur = cur.right 
        
        return root