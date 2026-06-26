class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # consider the matrix as a sorted list of ints
        # time complexity O(log m*n)
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows*cols)-1
        while l <= r:
            mid = (l+r) // 2
            row = mid // cols
            col = mid % cols
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False