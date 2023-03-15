class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        colns=len(grid[0])
        rows=len(grid)
        
        for row in range(1):# this do prefix for first row
            for col in range(1,colns):
                grid[row][col]+=grid[row][col-1]
        
        for row in range(1):# this do suffix for second row
            for col in range(colns-2,-1,-1):
                grid[1][col]+=grid[1][col+1]
      
        robot2=float("inf")
        for row in range(1):
            for col in range(colns):
                robot2=min(robot2,max(grid[row][colns-1]-grid[row][col],grid[row+1][0]-grid[row+1][col]))
        return robot2
                
                
        
