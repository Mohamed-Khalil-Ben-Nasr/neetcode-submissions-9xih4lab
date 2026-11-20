class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [ [0] * (cols+1) for i in range(rows+1)]
        for row in range(rows):
            rowPrefix = 0
            for col in range(cols):
                rowPrefix += matrix[row][col]
                self.sumMatrix[row+1][col+1] = rowPrefix + self.sumMatrix[row][col+1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        above = self.sumMatrix[row1-1][col2]
        left = self.sumMatrix[row2][col1-1]
        topLeft = self.sumMatrix[row1-1][col1-1]
        total = self.sumMatrix[row2][col2]
        return total - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)