class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        max_val=[]
        count=0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))


        def dfs(row,col,visited):
            nonlocal count
            nonlocal max_val
            
            if  visited[row][col]:
                return 
            visited[row][col]=True
            for row_change,col_change in  directions:
                new_row= row + row_change
                new_col = col + col_change
                if  inbound(new_row,new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col]:
                        dfs(new_row,new_col,visited)
                        count+=1
                        max_val.append(count)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] and not visited[row][col]:
                    count=1
                    max_val.append(count)
                    dfs(row,col,visited)
        if not max_val:
            return 0
        return max(max_val)


   








       
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col]:
                    dfs()