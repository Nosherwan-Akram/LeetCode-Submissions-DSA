# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
- 3 pointers -fast,slow,rev
- 1 stack array to contain new order
- loop over list using fast and slow to reach mid also reverse the first portion of
    list along the way
- add values to stack now till rev is null and slow is null
    - first add slow's value then rev's value
- pop stack until empty in the new list
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return
        fast,slow,rev = head,head,None
        stack = []
        while fast and fast.next:
            fast = fast.next.next
            current, slow = slow, slow.next
            current.next, rev = rev, current
        if fast:
            temp = slow
            slow = slow.next
            temp.next = None
        while slow or rev:
            if slow:
                stack.append(slow.val)
                slow = slow.next
            if rev:
                stack.append(rev.val)
                rev = rev.next
        current = head
        print(stack)
        while stack:
            current.val = stack.pop()
            if stack:
                current.next = ListNode()
                current = current.next
        if fast: current.next = temp