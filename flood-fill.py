class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        start_pixcel=grid[sr][sc]

        def dfs(row,col,visited):
        
            
            if  visited[row][col]:
                return 
            visited[row][col]=True
            grid[row][col]=color
            for row_change,col_change in  directions:
                new_row= row + row_change
                new_col = col + col_change
                if  inbound(new_row,new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col]==start_pixcel:
                        dfs(new_row,new_col,visited)
                        
    
        dfs(sr,sc,visited)
        return grid