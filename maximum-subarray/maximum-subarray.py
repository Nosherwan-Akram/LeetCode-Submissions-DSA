'''
maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6
can there be anything other than an array or array of floats?
what about empty array?
what if there exists more than 1 subarray that gives same sum?
should I be working towards time opitmization or space optimization? which is more imp?
input: Array of ints
output sum of largest sub array

edgecase = []
is it sorted?

Naive way: 
have a maxSum var
Nested for loops, from start to end of array for each loop
add the sum of current element in the for loop and store the max of maxSum and currentSum in maxSum
return maxSum at end
O(n^2) O(1)

Better way:
macSum = -99999
[-2,1,-3,4,-1,2,1,-5,4]

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -99999
        currSum = -99999
        for num in (nums):
            currSum = max(currSum+num,num)
            maxSum = max(currSum,maxSum)
        return maxSum