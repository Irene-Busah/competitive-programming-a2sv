# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Determine part sizes
        part_size = length // k
        extra = length % k
        
        result = []
        curr = head
        
        for i in range(k):
            part_head = curr
            size = part_size + (1 if extra > 0 else 0)
            if extra > 0:
                extra -= 1
            
            # advance to the end of the current part
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            
            # cut the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            result.append(part_head)
        
        return result
        