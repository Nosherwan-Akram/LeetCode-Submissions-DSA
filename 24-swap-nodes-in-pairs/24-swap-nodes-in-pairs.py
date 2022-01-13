# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
first check if we have only one node or zero node then return head
set follower to head and leadr to head.next
loop True
leader.val, folloer.val = follower.val, leader.val
if leader.next and leader.next.next
    follower = leader.next
    leader = leader.next.next
else
    return head
O(n) time
O(1) space

'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        follower = head
        leader = head.next
        while True:
            leader.val, follower.val = follower.val, leader.val
            if leader.next and leader.next.next:
                follower = leader.next
                leader = leader.next.next
            else:
                return head
        