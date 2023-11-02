# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        
        # current and previous
        previous = current = ListNode(None)
        current.next = head

        # find left
        for _ in range(left-1): previous = previous.next

        tail = previous.next

        # iterate until right
        for _ in range(right-left):
            next = previous.next
            previous.next = tail.next
            tail.next = tail.next.next
            previous.next.next = next

        return current.next
