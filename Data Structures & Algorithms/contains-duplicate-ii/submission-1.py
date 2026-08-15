class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # time complexity: O(n*k)
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                if j < len(nums) and nums[i] == nums[j]:
                    return True
        return False
