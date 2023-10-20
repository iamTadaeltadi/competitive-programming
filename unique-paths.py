class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        drn=[(0,1),(1,0)]
        memo=defaultdict(int)



        def inbound(row,col):
            return 0<=row<m and 0<=col<n
        

        def dp(r,c):

            if (r,c) in memo:
                return memo[(r,c)]
            
            if r==m-1 or c==n-1:
                return 1

            
                

            if inbound(r+1,c): 
                memo[(r,c)] += dp(r+1,c)

            if inbound(r,c+1): 
                memo[(r,c)] +=dp(r,c+1)

            return memo[(r,c)]
            
                
           
        return dp(0,0)