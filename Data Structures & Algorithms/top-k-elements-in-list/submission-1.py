from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCount = {}
        for num in nums:
            numToCount[num] = numToCount.get(num,0) + 1
        
        countToNums = defaultdict(list)
        for num, count in numToCount.items():
            countToNums[count].append(num)
        
        # max frequency = len(nums)
        m = len(nums)
        l = 0
        res = []
        while l < k:
            if m not in countToNums:
                m -= 1
                continue
            for num in countToNums[m]:
                res.append(num)
                l += 1
                if l == k:
                    return res
            m -= 1

        

        
