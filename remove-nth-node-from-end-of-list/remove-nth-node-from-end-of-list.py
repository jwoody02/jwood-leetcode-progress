# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        node_to_remove = None
        tmp_array = []
        
        i = 1
        while (node is not None):
            tmp_array.append(node)
            node = node.next
        node_to_remove = tmp_array[len(tmp_array) - n]
        index = tmp_array.index(node_to_remove)
        if index is not 0:
            tmp_array[index-1].next = node_to_remove.next
        del tmp_array[index]
        return tmp_array[0] if len(tmp_array) > 0 else None