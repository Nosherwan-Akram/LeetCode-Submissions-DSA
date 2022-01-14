# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        for i in range(0,len(arr),k):
            if k+i<=len(arr):
                arr[i:k+i] = arr[i:k+i][::-1]
        current = head
        for i in arr:
            current.val = i
            current = current.next
        return head