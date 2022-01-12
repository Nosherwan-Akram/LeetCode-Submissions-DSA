# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
input: linked list, what is in this list? only integers? what happends if empty,float,sorted,negative,range of the list? what if n is more than the llist? ncan be negative or not?
output: node

Efficient or Memory sufficient?

Solution:
current node pointing to head
loop over the list to find out the length
if lenght = n then set head to head.next
x = subtract nth from lenght
current set to head again
loop over list x
set current.next = current.next.next

code:
current = head
l = 0
while current:
    current = current.next
    l += 1
nodeToDelete = l - n
if nodeToDelete == 0:
    head = head.next
    return
current = head
i = 0
while i != nodeToDelete:
    current = current.next
current.next = current.next.next
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        l = 0
        while current:
            current = current.next
            l += 1
        nodeToDelete = l - n
        if nodeToDelete == 0:
            head = head.next
            return head
        current = head
        i = 0
        while i != nodeToDelete-1:
            current = current.next
            i += 1
        current.next = current.next.next
        return head
        