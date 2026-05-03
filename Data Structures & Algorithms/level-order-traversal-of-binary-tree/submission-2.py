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
        next_q = []
        toAdd = [] 
        final = []
        while q:
            for node in q:
                toAdd.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
                
            q = next_q
            next_q = []
            final.append(toAdd)
            toAdd = []
        return final

        # TC = O(n), SC = O(width)
            
