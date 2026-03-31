from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = defaultdict(int)

        for i,num in enumerate(nums):
            t = target - num
            if t in numToIndex:
                return [numToIndex[t], i]
            else:
                numToIndex[num] = i

