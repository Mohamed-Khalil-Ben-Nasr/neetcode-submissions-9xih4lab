class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]

        suf = [1 for i in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        res = [1 for i in range(len(nums))]
        for i in range(len(res)):
            res[i] = pref[i] * suf[i]
        
        return res
