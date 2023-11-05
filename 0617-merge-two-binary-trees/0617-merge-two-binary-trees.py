# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # main cases
        # 1) root1 is None at current position
        # 2) root2 is None at current position
        # 3) both root1 and root2 exist at current position

        # if one root doesn't exist, return the other
        if not root1:
            return root2
        if not root2:
            return root1

        # add root1 and root2
        newnode = TreeNode(root1.val + root2.val)
        newnode.left = self.mergeTrees(root1.left, root2.left)
        newnode.right = self.mergeTrees(root1.right, root2.right)

        # return new node
        return newnode
        