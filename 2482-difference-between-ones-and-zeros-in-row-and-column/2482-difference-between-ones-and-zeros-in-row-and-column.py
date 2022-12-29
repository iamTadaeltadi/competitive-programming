class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(grid), len(grid[0])
        res = [[0 for i in range(col+1)] for j in range(row + 1)]
        for r in range(1,row+1):
            for c in range(1,col+1):
                res[r][c] = res[r-1][c] + res[r][c-1] - res[r-1][c-1] + grid[r-1][c-1]
        
        for r in range(1,row+1):
            for c in range(1,col+1):
                grid[r-1][c-1] = 2*((res[-1][c] - res[-1][c-1]) + (res[r][-1] - res[r-1][-1])) - row - col
        return grid
                
