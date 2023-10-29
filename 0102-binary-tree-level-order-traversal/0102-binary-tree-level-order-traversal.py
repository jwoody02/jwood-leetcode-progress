# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        # BFS queue with the format: (level, node)
        queue = [(0, root)]

        # return array
        node_vals = []

        # iterate until queue empty
        while queue:
            level, current_node = queue.pop(0)

            if level < len(node_vals): node_vals[level] += [current_node.val]
            else: node_vals.append([current_node.val])

            # add subnodes to queue
            if current_node.left:
                queue.append((level + 1, current_node.left))
            if current_node.right:
                queue.append((level + 1, current_node.right))
        
        return node_vals
