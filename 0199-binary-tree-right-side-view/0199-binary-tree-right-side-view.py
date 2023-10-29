# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        # queue, which will be replaced at each level
        queue = [root]

        # return array
        right_values = []

        # iterate until empty queue
        while queue:
            right_most_val = queue[-1]
            right_values.append(right_most_val.val)

            queue = [child for node in queue for child in (node.left, node.right) if child]

        return right_values