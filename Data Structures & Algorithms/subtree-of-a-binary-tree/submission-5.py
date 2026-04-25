# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def issame(self, p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.issame(p.left, q.left) and self.issame(p.right, q.right )

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        
        if self.issame(root,subroot):
            return True
        
        return (self.isSubtree(root.left, subroot) or
        self.isSubtree(root.right, subroot))
       
        


        