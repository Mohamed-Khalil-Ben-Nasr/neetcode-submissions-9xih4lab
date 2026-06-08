class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if we can reach the goal from position i, 
        # then we just need to reach position i
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0