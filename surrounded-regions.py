class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        visited=[[False for i in range(len(board[0]))]for r in range(len(board))]     
        ans=[True]
        v=[]
        def inbound(row,col):
            return 0<=row<len(board) and 0<=col<len(board[0]) 
        def dfs(row,col):
            if visited[row][col]:
                return
            visited[row][col]=True
            v.append([row,col])
            if row==0 or col==0 or row==len(board)-1 or col==len(board[0])-1:
                ans[-1]=False
            for r,c in directions:
                new_row=row+r
                new_col=col+c
                if inbound(new_row,new_col) and board[new_row][new_col]=="O":
                    
                    dfs(new_row,new_col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=="O" and not visited[row][col]:
                    ans=[True]
                    v=[]
                    dfs(row,col)
                    if ans[-1]:
                        for r,c in v:
                            board[r][c]="X"