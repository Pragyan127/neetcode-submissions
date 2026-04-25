# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        nextq, res, h = [], [], []
        while q:
            for node in q:
                h.append(node.val)
                if node.left:
                    nextq.append(node.left)
                if node.right:
                    nextq.append(node.right)    
            res.append(h)
            h = []
            q= nextq
            nextq = []

        return res


        