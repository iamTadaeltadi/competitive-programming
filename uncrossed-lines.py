class Solution:
    def maxUncrossedLines(self, num1: List[int], num2: List[int]) -> int:


        cache ={}
        

        def dp(i,j):

            if i==len(num1) or j==len(num2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            if num1[i] == num2[j]:
                cache[(i,j)] = 1+ dp(i+1,j+1)
            else:
                cache[(i,j)] = max(dp(i,j+1),dp(i+1,j))

            return cache[(i,j)]

        return dp(0,0)