class Solution(object):
    def setZeroes(self, matrix):
        
        columns=len(matrix[0])
        rows=len(matrix)
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    
                    for r in range(columns):
                        if matrix[i][r]!=0:
                            matrix[i][r]="a"
                            
                        
                    for c in range(rows):
                        if matrix[c][j]!=0:
                            matrix[c][j]="a"
                        
                        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]=="a":
                    matrix[i][j]=0
                    
        print(matrix)
                        
                        
                    
                    
                    
                
                    
                    
                    
                
                
                
