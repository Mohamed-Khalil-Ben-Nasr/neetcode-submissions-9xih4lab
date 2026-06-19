class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums2)
        for i in range(len(nums2)-2, -1,-1):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    nextGreater[i] = nums2[j]
                    break

        numToIndex = {}
        for i,num in enumerate(nums2):
            numToIndex[num] = i

        res = []
        for num in nums1:
            j = numToIndex[num]
            res.append(nextGreater[j])
        
        return res