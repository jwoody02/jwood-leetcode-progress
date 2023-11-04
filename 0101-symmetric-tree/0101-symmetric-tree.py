# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areTreesMirrored(q: Optional[TreeNode], p: Optional[TreeNode]):
            if q and not p: return False
            if p and not q: return False
            if not p and not q: return True

            return p.val == q.val and areTreesMirrored(q.left, p.right) and areTreesMirrored(q.right, p.left)
        
        return areTreesMirrored(root.left, root.right)