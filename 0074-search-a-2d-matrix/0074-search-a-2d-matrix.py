class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenOfRow=len(matrix)
        lenOfCol=len(matrix[0])
        
        for row in range(lenOfRow):
            if target >=matrix[row][0] or target<=matrix[row][lenOfCol-1]:
                for col in range((lenOfCol)):
                    if matrix[row][col]==target:
                        return True
        return False
                