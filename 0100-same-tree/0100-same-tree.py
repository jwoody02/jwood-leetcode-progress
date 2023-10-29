# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True # base case when both are none, end bfs
        if not p or not q: return False # only one is none
        if p.val != q.val: return False # values not equal

        subTreesEqual = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return subTreesEqual
        

