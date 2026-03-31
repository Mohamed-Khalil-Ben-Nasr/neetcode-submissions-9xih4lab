class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums) 
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = [1] * len(nums)
        suf[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = pre[i] * suf[i]
        
        return output
             