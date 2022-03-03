class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        sum_ = 0
        for i in range(len(matrix)):
            self.prefix.append([])
            for j in range(len(matrix[i])):
                sum_ += matrix[i][j]
                self.prefix[i].append(sum_)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1,row2+1):
            sum_ += self.prefix[i][col2] - self.prefix[i][col1] + self.matrix[i][col1]
        return sum_
    
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
