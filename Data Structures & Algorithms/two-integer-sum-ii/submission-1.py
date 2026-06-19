class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        # since we cant use the same element twice, we cant consider
        # the solution where the two pointers meet at the middle
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1
            