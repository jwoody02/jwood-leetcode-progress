# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def isLeaf(root):
            return not root.left and not root.right

        # modified DFS to return minimum depth
        def minDepthDFS(root, depth) -> int:
            # base case
            if not root or isLeaf(root): return depth + 1
            
            # get left and right depths
            leftDepth = pow(2, 31)
            rightDepth = pow(2, 31)
            if root.left:
                leftDepth = minDepthDFS(root.left, depth + 1)
            if root.right:
                rightDepth = minDepthDFS(root.right, depth + 1)
            return min(leftDepth, rightDepth)

        # return minimum depth
        return minDepthDFS(root, 0)