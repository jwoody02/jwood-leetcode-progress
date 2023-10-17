# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # variable to store diameter
        diameter = 0

        # dfs to get longest length
        def dfs(node) -> int:
            nonlocal diameter

            # by default return 0
            if not node:
                return 0

            # get left and right depths
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # update diameter
            diameter = max(diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return diameter