# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
l1,l2 will only contain integers? positive integers? sorted? float? aplphbets? range?
what will be the inputs?
output: a linked list of sum
example : 2-4-3 + 5-6-4 = 7-0-8

what is important time or memory?

Naive:
go through list 1
add the digits of each node after multiplying them by 10 for each node jumped
2*10^0 + 4*10^1 + 3*10^2
store it and repeat for the other list
and then add the two numbers and have a modular division to get single digits and store them in new list
807%10 = 7
800%100 = 0
800%1000 = 8
0 is reached so I stop
time O(max(n,m))
space O(max(n,m))

2  4  3
5  6  4 7

7  0  8 7

p1, p2 pointing at the start of each list
do while loop until the next of both pointers is null
at each iteration add the digits+carry from last time
do modular division and store the value in new node
do whole divison and store carry for next addition
current's next should point to the new node 
update the current's next to new node
make current the current's next

p1 = l1
p2 = l2
carry = 0
newHead = ListNode(0)
current = newHead
while p1 or p2:
    digitSum = carry
    if p1:
        digitSum += p1.val
    if p2:
        digitSum += p2.val
    carry = digitSum//10
    nodeVal = digitSum%10
    current.value = nodeVal
    if p1.next or p2.next:
        current.next = ListNode(0)
        current = current.next
    if p1:
        p1 = p1.next
    if p2:
        p2 = p2.next
return newHead

[7,0,] 1
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        newHead = ListNode(0)
        current = newHead
        while p1 or p2:
            digitSum = carry
            if p1:
                digitSum += p1.val
            if p2:
                digitSum += p2.val
            carry = digitSum//10
            nodeVal = digitSum%10
            current.val = nodeVal
            if (p1 and p1.next) or (p2 and p2.next):
                current.next = ListNode(0)
                current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry!=0:
            current.next = ListNode(carry)
        return newHead
        