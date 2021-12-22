class Solution:
    def twoSum(self, array: List[int], target: int) -> List[int]:
        compDict = {}
        for i in range(len(array)):
            if array[i] in compDict:
                return [i,compDict[array[i]]]
            else:
                compDict[target-array[i]] = i
        return False