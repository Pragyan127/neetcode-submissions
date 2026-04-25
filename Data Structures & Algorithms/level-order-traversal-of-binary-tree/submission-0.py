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

        queue = [root]
        result, level, next_queuq = [],[],[]

        while queue:
            for root in queue:
                level.append(root.val)

                if root.left:
                    next_queuq.append(root.left)
                if root.right:
                    next_queuq.append(root.right)
            result.append(level)
            queue = next_queuq
            next_queuq = []
            level = []
        return result


        