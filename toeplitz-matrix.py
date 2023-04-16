class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows=len(matrix)-1
        cols=len(matrix[0])-1

        for row in range(rows):
            for col in range((cols)):
                if matrix[row][col]!=matrix[row+1][col+1]:
                    return False

        return True