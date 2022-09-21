class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans, n = 0, len(piles)
        for i in range(n - 2, n // 3 - 1, -2):
            ans += piles[i]
        return ans
