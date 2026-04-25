# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        

        # return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
        if not root:
            return 0
        q = deque()
        high = 0
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            high += 1
        return high

                
            

