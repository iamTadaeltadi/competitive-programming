class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        queue=deque()
        ans=[[ 0 for col in range(len(mat[0]))] for row in range(len(mat))]
        visit=set()
        def inbound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==0:
                    queue.append((row,col,0))
                    visit.add((row,col))
        dirn=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            row,col,path=queue.popleft()
            if mat[row][col]==1:
                ans[row][col]=path
                
            for  r,c in dirn:
                new_row=r+row
                new_col=c+col
                if inbound(new_row,new_col) :
                    if (new_row,new_col) not in visit:
                        queue.append((new_row,new_col,path+1))
                        visit.add((new_row,new_col))
        return ans