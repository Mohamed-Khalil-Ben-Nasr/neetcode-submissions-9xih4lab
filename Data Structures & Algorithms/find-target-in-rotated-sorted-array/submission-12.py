class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r :
            m = (l + r) // 2
            print(m)
            if nums[m] == target:
                return m
            # if left portion is sorted
            elif nums[l] <= nums[m]:
                # if target in left portion
                if nums[l] <= target < nums[m]:
                    # => search left
                    r = m - 1
                else:
                    # search right portion
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1