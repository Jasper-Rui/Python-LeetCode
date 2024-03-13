# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        tmp = head

        while tmp and tmp.next:
            if tmp.next.val is val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head.next if head and head.val is val else head

