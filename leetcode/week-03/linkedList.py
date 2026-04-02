
"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended 
to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class MyLinkedList:

#     def __init__(self):
#         self.head = None
        

#     def get(self, index: int) -> int:
#         current = self.head

#         for i in range(index):
#             if not current:
#                 return -1
            
#             current = current.next
        
#         if current:
#             return current.val
#         else:
#             return -1
        

#     def addAtHead(self, val: int) -> None:
#         new_node = ListNode(val)
#         new_node.next = self.head

#         self.head = new_node


#     def addAtTail(self, val: int) -> None:
#         new_node = ListNode(val)

#         if not self.head:
#             self.head = new_node
#             return

#         current = self.head
#         while current.next:
#             current = current.next
        
#         current.next = new_node


#     def addAtIndex(self, index: int, val: int) -> None:

#         if index == 0:
#             self.addAtHead(val)
#             return

#         current = self.head

#         for _ in range(index - 1):
#             if not current:
#                 return
            
#             current = current.next

#         if not current:
#             return

#         new_node = ListNode(val)
#         new_node.next = current.next
#         current.next = new_node
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index == 0:
#             if self.head:
#                 self.head = self.head.next
#             return

#         current = self.head
#         for _ in range(index - 1):
#             if not current:
#                 return
            
#             current = current.next
        
#         if not current or not current.next:
#             return
        
#         current.next = current.next.next





"""
Given the head of a singly linked list, reverse the list, and return 
the reversed list.
"""  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         previousNode = None
#         currentNode = head
#         while currentNode != None:
#             nextItem = currentNode.next
#             currentNode.next = previousNode
#             previousNode = currentNode
#             currentNode = nextItem
#         return previousNode


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
            
#             tail = tail.next
        
#         if list1:
#             tail.next = list1
#         if list2:
#             tail.next = list2

#         return dummy.next
    

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def printLinkedList(head):
#     current = head

#     while current:
#         print(current.data)
#         current.next



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



        




