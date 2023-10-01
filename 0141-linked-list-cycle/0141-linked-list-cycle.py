# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()

        while head != None:
            if head in visited_nodes:
                return True
            if head.next is None:
                return False
            visited_nodes.add(head)
            head = head.next

        return False