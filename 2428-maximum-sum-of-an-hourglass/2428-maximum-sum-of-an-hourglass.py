class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x=0
        m=0
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                x=0
                x+=grid[j][i] +grid[j][i+1]+grid[j][i+2]
                x+=grid[j+1][i+1]
                x+=grid[j+2][i] +grid[j+2][i+1]+grid[j+2][i+2]
                m=max(x,m)
        return m
    
        