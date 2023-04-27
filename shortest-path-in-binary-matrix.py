class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1

        queue=deque([(0,0,1)])
        dirn=[(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
        visited = set((0, 0))
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])



        while queue:
            
            c_row,c_col,path=queue.popleft()
            
            
            if c_row==len(grid)-1 and c_col==len(grid[0])-1:
                return path
            for r,c in dirn:
                new_row=c_row+r
                new_col=c_col+c
                if inbound(new_row,new_col) and (new_row,new_col)  not in visited and grid[new_row][new_col] ==0:
                    queue.append((new_row,new_col,path+1))
                    visited.add((new_row,new_col))

        return -1