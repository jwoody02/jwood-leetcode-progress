# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #BFS
        queue = [root]
        elements = []

        while queue:
            item = queue.pop(0)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

            elements.append(item.val)

        # now sort elements O(nlogn)
        elements.sort()

        # return kth smallest
        return elements[::-1][-k]
       
        

        
            
            