class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res=0
        matrix=[ [strs[col][row] for row in range(len(strs[col]))] for col in range(len(strs)) ]
        
        for col in range(len(matrix[0])):
            for row in range(1,len(matrix)):
                if matrix[row][col] <matrix[row-1][col]:
                    res+=1
                    break
        return res
                
                