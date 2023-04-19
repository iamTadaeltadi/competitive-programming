class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):

                sum_row=[0,0,0]
                sum_col=[0,0,0]
                sum_diagonal=0
                distinct=set()
                duplicated=False
                for r in range(row,row+3):
                    sum_row[r-row]+=sum(grid[r][col:col+3])

                    for c in range(col,col+3):
                        if grid[r][c] in distinct or grid[r][c]>9 or  grid[r][c]==0:
                            duplicated=True
                        distinct.add(grid[r][c])
                        
                        sum_col[c-col]+=grid[r][c]
                        
                        if  r-row ==c-col or  2-(c-col)==r-row:

                            sum_diagonal+=grid[r][c]

                        if  r-row ==c-col and   2-(c-col)==r-row:

                            sum_diagonal+=grid[r][c]

                if not duplicated and sum_row[0]==sum_row[1]==sum_row[2]==sum_col[0]==sum_col[1]==sum_col[2]:
                    if sum_diagonal//2==sum_row[0]:
                        ans+=1
        return ans