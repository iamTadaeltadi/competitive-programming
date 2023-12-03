class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        visited = set() 

        def dfs(curr_x, curr_y):
            visited.add((curr_x, curr_y))
            for dir_x, dir_y in directions:
                next_x, next_y = curr_x + dir_x, curr_y + dir_y 
                if next_x in range(len(grid)) and next_y in range(len(grid[0])) and grid[next_x][next_y] == "1" and (next_x, next_y) not in visited:
                    dfs(next_x, next_y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    output += 1 
                    dfs(i, j)

        return output 