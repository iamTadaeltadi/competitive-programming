class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        visited=set()
        queue=deque()
        queue2=deque()
        isOne=False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    queue.append((row,col))
                    grid[row][col]=2
                    queue2.append((row,col,0))
                    isOne=True
                    visited.add((row,col))
                    break
            if isOne:
                break
                

        dirn=[(1,0),(-1,0),(0,-1),(0,1)]
        
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        while queue:
            c_row,c_col=queue.popleft()
            for r,c in dirn:
                new_row=c_row+r
                new_col=c_col+c

                if inbound(new_row,new_col)  and grid[new_row][new_col] ==1:
                    queue.append((new_row,new_col))
                    grid[new_row][new_col]=2
                    queue2.append((new_row,new_col,0))
                    visited.add((new_row,new_col))
        print(visited)
        print(grid)
        print(queue2)
        while queue2:
            
            c_row,c_col,path=queue2.popleft()
            # print(c_row,c_col)
            if grid[c_row][c_col]==1:
                return path -1
                
           
            for r,c in dirn:
                new_row=c_row+r
                new_col=c_col+c

                if inbound(new_row,new_col) and (new_row,new_col)  not in visited :
                    visited.add((new_row,new_col))
                    queue2.append((new_row,new_col,path+1))
        return 0