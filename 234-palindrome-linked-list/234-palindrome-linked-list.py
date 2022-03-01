# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        l = 0
        while curr:
            l+=1
            stack.append(curr.val)
            curr = curr.next
        return stack == stack[::-1]
            