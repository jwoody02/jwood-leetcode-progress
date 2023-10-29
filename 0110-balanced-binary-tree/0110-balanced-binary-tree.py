# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return value
        balanced = True

        # dfs to find heights of all subtrees starting at node
        def dfs(node) -> int:
            # found leaf, return 0
            nonlocal balanced
            if not node: return 0

            # get heights for left and right subtrees
            right_height, left_height = dfs(node.right), dfs(node.left)

            # if difference between the heights > 1, then it's not balanced
            if abs(right_height - left_height) > 1: balanced = False

            # return right height + left + 1 to account for this node
            return max(right_height, left_height) + 1

        # start dfs
        dfs(root)
        return balanced