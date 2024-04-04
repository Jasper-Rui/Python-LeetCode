# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        node1 = head
        node2 = head.next

        node1.next = node2.next
        node2.next = node1
        head = node2

        if node1.next is None:
            return head

        last_node = node1
        node1 = node1.next
        node2 = node1.next

        while node1 is not None and node2 is not None:
            node1.next = node2.next
            node2.next = node1
            last_node.next = node2

            last_node = node1
            node1 = node1.next
            if node1 is None:
                break
            node2 = node1.next

        return head
