"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = [head]
        dummyNode = Node(0)
        prev = dummyNode
        while stack:
            curr = stack.pop()
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            
            curr.prev = prev
            prev.next = curr
            curr.child = None
            prev = curr
        dummyNode.next.prev = None
        return dummyNode.next
        