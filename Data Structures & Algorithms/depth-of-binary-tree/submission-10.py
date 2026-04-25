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
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+max(left, right)
# #if the tree is enpty
#         if not root:
#             return 0
#         #creating a dqueue for BFS
#         q= deque()
#         #initially level is 0, no node visited
#         level = 0

#         #if root is available append to queue
#         if root:
#             q.append(root)
#         #travers over tree level by level
#         while q:
#             #no of nodes in current level
#             for i in range(len(q)):
#                 node = q.popleft()
#                 #add the child node towards left
#                 if node.left:
#                     q.append(node.left)
#                 #add the children node towards right
#                 if node.right:
#                     q.append(node.right)
#             #after each successfull iteration level value is increased by 1
#             level += 1
#         return level

        # return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)


