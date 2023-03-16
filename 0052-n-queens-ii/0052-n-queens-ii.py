class Solution:
    def totalNQueens(self, n: int) -> int:
        grid=[[ 0 for i in range(n)]  for i in range(n) ]
        
        def helper(row,col):
            for r in range(0,row):
                
                if grid[r][col]==1:
                    return False
            row1=row
            col1=col
            while row1 <n and col1<n:
                if grid[row1][col1]==1:
                    return False
                row1-=1
                col1+=1
            while row >=0and col>=0:
                if grid[row][col]==1:
                    return False
                row-=1
                col-=1
            return True
            
            
        res=0
        def queen(row,count):
            nonlocal res
            for i in range(n):
                
                
                if row==n and i==n:
                    return
                if count==n :
                    res+=1
                    return 
                if helper(row,i):
                    count+=1
                    grid[row][i]=1
                    queen(row+1,count)
                    grid[row][i]=0
                    count-=1
        queen(0,0)
        return res
                
            
            
        