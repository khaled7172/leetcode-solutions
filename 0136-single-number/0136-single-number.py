class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
        for key, value in numDict.items():
            if value == 1:
                return key
        