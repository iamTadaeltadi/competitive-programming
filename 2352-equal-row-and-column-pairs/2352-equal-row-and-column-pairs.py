class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        equals=0
        columns=len(grid[0])
        transpose=[]
        for column in range(columns):
            listt=[]
            for row in range(rows):
                listt.append((grid[row][column]))
            transpose.append(listt)
        print(transpose)
        for row in  grid:
            for r in transpose:
                if row==r:
                    equals+=1

        return equals