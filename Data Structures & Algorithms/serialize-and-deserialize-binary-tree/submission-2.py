# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []
        def dfs(root):
            if not root:
                ser.append('N')
                return
            ser.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        ser = ",".join(ser)
        return ser

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # if not data:
        #     return None
        ser = data.split(',')
        self.i = 0
        def dfs():
            if ser[self.i] == 'N':
                self.i += 1
                return None
            root = TreeNode[ser[self.i]]
            root.left = dfs()
            root.right = dfs()
        return root
