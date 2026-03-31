class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre,suf = [1] * l, [1] * l
        pre[0] = 1
        suf[l-1] = 1

        for i in range(1,l,1):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(l-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        
        output = [1] * l
        for i in range(l):
            output[i] = pre[i] * suf[i]
        
        return output