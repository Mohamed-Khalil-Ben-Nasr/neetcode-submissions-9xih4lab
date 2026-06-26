class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the binary search in row is only triggered when we find 
        # the row where target might exist
        # time complexity => O(log m) to find row + O(log n) to find col once we find row
        # => O(log(m*n))
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows-1
        while l <= r:
            # find the row where target exists
            # => O(log m)
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                # find the col where target exists
                # => O(log n)
                lc, rc = 0, cols-1
                while lc <= rc:
                    m = (lc + rc) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        rc = m - 1
                    else:
                        lc = m + 1
                # target col not found
                return False
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        # target row not found
        return False
            