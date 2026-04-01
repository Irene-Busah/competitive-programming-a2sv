# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                # cycle = True
                break
        else:
            return None
        
        slow = head

        while slow != fast:
            head = head.next
            slow = slow.next

        return slow