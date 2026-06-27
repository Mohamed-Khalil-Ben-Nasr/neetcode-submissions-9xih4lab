class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        initialized = False
        increasing = True
        for i in range(len(nums)-1):
            if not initialized:
                if nums[i] == nums[i+1]:
                    continue
                elif nums[i] > nums[i+1]:
                    increasing = False
                    initialized = True
                else:
                    initialized = True
            if initialized:
                if increasing:
                    if nums[i] > nums[i+1]:
                        return False
                else:
                    if nums[i] < nums[i+1]:
                        return False
        return True