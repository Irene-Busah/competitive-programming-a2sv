class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current = self.head

        for i in range(index):
            if not current:
                return -1
            
            current = current.next
        
        if current:
            return current.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head

        self.head = new_node


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
            return

        current = self.head

        for _ in range(index - 1):
            if not current:
                return
            
            current = current.next

        if not current:
            return

        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            
            current = current.next
        
        if not current or not current.next:
            return
        
        current.next = current.next.next