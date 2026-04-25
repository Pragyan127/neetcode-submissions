# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # q = deque()
        # q.append(root)

        # h = 0

        # while q:
        #     for i in range(len(q)):
        #         root = q.popleft()

        #         if root.left:
        #             q.append(root.left)
        #         if root.right:
        #             q.append(root.right)
        #     h += 1
        
        # return h

        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)


