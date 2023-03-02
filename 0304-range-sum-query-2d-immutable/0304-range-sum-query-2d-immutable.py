class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        
        
        rows=len(matrix)
        colns=len(matrix[0])
        prefix=[[0 for i in range(colns+1)] for i in range(rows+1)]
        for r in range(rows):
            for c in range(colns):
                prefix[r+1][c+1]=matrix[r][c] +prefix[r+1][c] +prefix[r][c+1]-prefix[r][c]
        self.prefix=prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix=self.prefix
        return prefix[row2+1][col2 +1] -prefix[row1][col2+1] -prefix[row2+1][col1] +prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)