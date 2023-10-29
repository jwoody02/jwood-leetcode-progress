# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return val
        subTree = False

        # helper function to check if two trees equal
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q: return True # both p and q are leaves
            if not p or not q: return False # only one is leaf
            if p.val != q.val: return False # values are not equal

            # check subtrees if equal
            leftTreeEqual = isSameTree(p.left, q.left)
            rightTreeEqual = isSameTree(p.right, q.right)

            return leftTreeEqual and rightTreeEqual
        
        # value to search for nodes with same value
        target_value = subRoot.val

        def dfs(root_node: Optional[TreeNode], target: int):
            nonlocal subTree

            # exit if subtree already found OR root node is None
            if subTree or not root_node:
                return

            # found target root node and is same tree, our return val is now true
            if root_node.val == target and isSameTree(root_node, subRoot): 
                subTree = True
                return
            
            # call bfs on left and right nodes
            dfs(root_node.left, target)
            dfs(root_node.right, target)


        dfs(root, target_value)

        return subTree