class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (C+1) for _ in range((R+1))]
        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c+1]
                self.sum_matrix[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        br = self.sum_matrix[row2+1][col2+1]
        l = self.sum_matrix[row2+1][col1]
        t = self.sum_matrix[row1][col2+1]
        tl = self.sum_matrix[row1][col1]

        return br - t - l + tl


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)