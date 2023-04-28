class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue=deque([(entrance[0],entrance[1],0)])
        dirn=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        visited.add((entrance[0],entrance[1]))

        def inbound(row,col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])

        while queue:
            curr_row,curr_col,path=queue.popleft()
            

            for r,c in dirn:
                new_row=r+curr_row
                new_col=c+curr_col
                

                if inbound(new_row,new_col) and (new_row,new_col) not in visited and maze[new_row][new_col]==".":
                    queue.append((new_row,new_col,path+1))
                    print(new_row,new_col)
                    if new_row== len(maze)-1 or new_col==len(maze[0])-1 or new_row== 0 or new_col== 0 :
                        return path+1
                    visited.add((new_row,new_col))
        return -1