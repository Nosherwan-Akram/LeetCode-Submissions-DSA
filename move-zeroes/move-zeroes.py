'''
movezeros( input -> array of ints) output -> array

can we have negative numbers?
emoty arrays?
is it sorted?

what are space and efficiency?
naive way:
 for loop over array
 put the 


better way:
put elements as keys in dictionary
put their repition as the value
sort them
loop over the dictionary
  append the key into a new array the number of times its value is in dic
return new Array
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = p2 = 0
        while p1!=len(nums):
            if nums[p1]==0:
                p1+=1
            else:
                nums[p2] = nums[p1]
                p2+=1
                p1+=1
        for i in range(p2,p1):
            nums[i] = 0