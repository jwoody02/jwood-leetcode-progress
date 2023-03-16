# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # BST:
        # Left - All less than root
        # Right - All greater than root

        # Idea 1 - O(n) time complexity and O(n) memory complexity, where n = number of nodes
        # Step 1) Traverse tree and append values of nodes to array
        # Step 2) Compare this array to a sorted version of the array to find the swapped values
        # Step 3) Traverse the tree once more to find the two nodes and swap the values

        _node_values = [] # int array

        # traverse in order and return values
        def traversalForVals(root: Optional[TreeNode]) -> [int]:
            ret_arr = []
            if root is not None:
                ret_arr += traversalForVals(root.left)
                ret_arr.append(root.val)
                ret_arr += traversalForVals(root.right)
            return ret_arr
        # traverse and find node equal to value
        def findNodeWithValue(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            ret_val = None
            if root is not None:
                if root.val == val:
                    return root
                _left = findNodeWithValue(root.left, val)
                _right = findNodeWithValue(root.right, val)
                if _left is not None:
                    return _left
                if _right is not None:
                    return _right
            return None

        _node_values = traversalForVals(root)
        
        _sorted = sorted(_node_values) # sort integers for comparison
        _invalid_node_vals = [] # will contain the two values that are wrong
        for i in range(len(_node_values)):
            if _node_values[i] != _sorted[i]:
                _invalid_node_vals.append(_node_values[i])
        if len(_invalid_node_vals) < 2:
            return root
        
        node_1 = findNodeWithValue(root,_invalid_node_vals[0])
        node_2 = findNodeWithValue(root,_invalid_node_vals[1])
        
        node_1.val, node_2.val = node_2.val, node_1.val
        return root
            

        