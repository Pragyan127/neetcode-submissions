# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        def issymmetric(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return (issymmetric(p.right, q.right) and issymmetric(p.left, q.left))

        def has_subtree(root):
            if not root:
                return False
            if issymmetric(root, subroot):
                return True
            
            return (has_subtree(root.left) or has_subtree(root.right))

        return has_subtree(root)


