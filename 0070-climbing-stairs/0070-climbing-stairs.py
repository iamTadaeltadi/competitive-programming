class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:1, -1:0}
        def rec(n):
            if n in dp:
                return dp[n]
            dp[n] = rec(n - 2) + rec(n - 1)
            return dp[n]
        return rec(n)   