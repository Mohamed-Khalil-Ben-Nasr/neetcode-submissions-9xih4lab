class Solution:
    def rob(self, nums: List[int]) -> int:
        # since we cant rob first and last in the same spree/path
        # we consider both possibilites and pick the max
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]
        
        rob1, rob2 = 0, 0
        for i in range(len(nums1)):
            tmp = max(rob1 + nums1[i], rob2)
            rob1 = rob2
            rob2 = tmp
        
        rob3, rob4 = 0, 0
        for i in range(len(nums2)):
            tmp = max(rob3 + nums2[i], rob4)
            rob3 = rob4
            rob4 = tmp
        
        return max(rob2, rob4)