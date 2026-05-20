class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numToIndex:
                return [numToIndex[diff], i]
            numToIndex[num] = i
