# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal balanced

            # If the node is None, return the depth - 1
            if not node:
                return depth - 1

            # Get the depths of the two subtrees
            leftDepth = dfs(node.left, depth + 1)
            rightDepth = dfs(node.right, depth + 1)

            # If the difference in depths is greater than 1, set balanced to False
            if abs(leftDepth - rightDepth) > 1:
                balanced = False
            
            # Return the maximum depth
            return max(leftDepth, rightDepth)

        # Start DFS on the root node
        dfs(root, 0)
        return balanced

