class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid1[0]))] for j in range(len(grid1))]
        count=0

        
        def inbound(row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))


        ans = [True]
        def dfs(row,col,visited):
            
            if not grid1[row][col]:
                ans[0] = False

 
            for row_change,col_change in  directions:
                new_row= row + row_change
                new_col = col + col_change
                if  inbound(new_row,new_col) and not visited[new_row][new_col] and grid2[new_row][new_col]:
                    visited[new_row][new_col] = True
                    dfs(new_row,new_col,visited)
 

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                
                if not visited[row][col] and grid2[row][col] and grid1[row][col]:
                    visited[row][col] =True
                    ans = [True]
                    dfs(row,col,visited)
                    count += ans[0]
                    
        return count