class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[]
        for row in range(1,len(grid)-1):
            x=[]
            for col in range(1,len(grid[0])-1):
                max_val=0
                new_row=row-1
                new_col=col-1
                for r in range(new_row,new_row+3):
                    for c in range(new_col,new_col+3):
                        max_val=max(max_val,grid[r][c])
                x.append(max_val)
            ans.append(x)
        return ans