class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l<=r:
            # this portion of the array is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            # we are in the sorted portion of the greater numbers
            if nums[m] >= nums[l]:
                # seach right in the smaller numbers portion
                l = m + 1
            else:
                r = m - 1
        
        return res