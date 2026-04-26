# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mid_map = {val:i for i,val in enumerate(inorder)}

        self.idx = 0
        def dfs(left, right):
            if left>right:
                return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1

            mid = mid_map[root.val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            return root
        return dfs(0, len(inorder) - 1)

        #TC = O(N)
        #Sc = O(N)
        
