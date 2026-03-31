class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # O(n log n)
        nums.sort()

        # O(n^2)
        for i, num in enumerate(nums):
            if ( (i >0) and (nums[i] == nums[i-1])):
                continue
            l, r = i + 1, len(nums)-1
            # l and r can never be equal because we need two nums for our solution
            while l<r:
                threeS = num + nums[l] + nums[r]
                if threeS > 0:
                    r -= 1
                elif threeS < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    # now we need to adjust the pointers to see if we can find a different unique solution
                    # moving only one pointer is enough to make the new solution unique
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res