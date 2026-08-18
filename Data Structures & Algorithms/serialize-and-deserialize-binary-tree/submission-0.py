# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tc both is O(n)
# sc both is O(n)
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        # preorder dfs string comma seperated 
        def dfs(node: TreeNode):
            # base case
            if node == None:
                res.append("N")
                return 

            # recursion 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        # i.e "1,2,-1,0,N,N...."
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        # starting at i, build me ONE complete subtree an dleave i pointing just after it 
        # i.e essentially build the tree recursively usign the preorder array, you manage the pointer 
        # easier to draw out the array and tree to reason about when and where ot push the count
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node 

        return dfs()