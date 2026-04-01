# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        previousNode = dummy

        for i in range(1, left):
            previousNode = previousNode.next

        current = previousNode.next
        then = current.next

        for i in range(right-left):
            current.next = then.next
            then.next = previousNode.next
            previousNode.next = then

            then = current.next
        
        return dummy.next