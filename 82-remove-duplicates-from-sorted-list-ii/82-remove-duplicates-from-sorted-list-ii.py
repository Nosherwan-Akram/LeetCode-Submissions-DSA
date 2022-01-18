# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        newHead = ListNode(0)
        temp = newHead
        dic = {}
        while current:
            if current.val not in dic:
                dic[current.val] = 1
            else:
                dic[current.val] += 1
            current = current.next
        for k,v in sorted(dic.items()):
            if v == 1:
                temp.next = ListNode(k)
                temp = temp.next
        return newHead.next