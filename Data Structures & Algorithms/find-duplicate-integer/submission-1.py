class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the meeting point
        # they dont necessarily meet at the start of the cycle 
        # they can meet at any point in the cycle
        # starting from different starting positions will break the math formula
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # now initialize a new pointer slow 2
        # slow 2 and slow will meet at the start of the cycle
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow2
