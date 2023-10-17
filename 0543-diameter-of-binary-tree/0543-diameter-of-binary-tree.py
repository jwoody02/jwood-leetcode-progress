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
        # caching
        node_cache = {} # { node: depth }

        # dfs to get longest length
        def dfs(node) -> int:
            nonlocal diameter

            # by default return 0
            if not node:
                return 0

            # get left depth using node_cache if possible
            left_depth = 0
            if node.left in node_cache:
                left_depth = node_cache[node.left]
            else:
                left_depth = dfs(node.left)
                node_cache[node.left] = left_depth
            
            # get right depth using node_cache if possible
            right_depth = 0
            if node.right in node_cache:
                right_depth = node_cache[node.right]
            else:
                right_depth = dfs(node.right)
                node_cache[node.right] = right_depth

            # update diameter
            diameter = max(diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return diameter