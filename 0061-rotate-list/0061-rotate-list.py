# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # compute length and get tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # normalize k
        k %= length
        if k == 0:
            return head

        # find new tail
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next

        # set new head and break the list
        new_head = new_tail.next
        new_tail.next = None

        # connect old tail to old head
        tail.next = head

        return new_head