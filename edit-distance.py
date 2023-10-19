class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        self.memo = [[-1] * n for _ in range(m)]

        def dp(i, j):
            if i == -1:
                return j + 1

            if j == -1:
                return i + 1
            
            if self.memo[i][j] != -1:
                return self.memo[i][j]

            if word1[i] == word2[j]:
                self.memo[i][j] = dp(i - 1, j - 1)
            
            else:
                self.memo[i][j] = min(dp(i, j - 1), 
                                      dp(i - 1, j), 
                                      dp(i - 1, j - 1)) + 1
            return self.memo[i][j] 
        return dp(m - 1, n - 1)