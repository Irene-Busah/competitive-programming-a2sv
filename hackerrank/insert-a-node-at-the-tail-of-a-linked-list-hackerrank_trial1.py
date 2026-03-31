class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insertNodeAtTail(head, data):
    new_node = ListNode(data)
    
    if not head:
        return new_node
    
    current = head
    
    while current.next:
        current = current.next
    
    current.next = new_node
    
    return head