# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Go over list to find length
k = k % length
toMakeHead = lenght - k
if not head or head.next is none return head
prev = head
current = head.next
loop over list till to make new head
head = current
prev.next = none

'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        lenght = 0
        while current:
            current = current.next
            lenght += 1
        k = k % lenght
        toMakeNewHead = lenght - k
        if toMakeNewHead == 0 or k == 0:
            return head
        current = head
        for i in range(toMakeNewHead):
            temp = current
            current = current.next
        newHead = current
        while current and current.next:
            current = current.next
        current.next = head
        temp.next = None
        head = newHead
        return head