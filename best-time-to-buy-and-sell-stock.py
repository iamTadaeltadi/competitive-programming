class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        r=prices[0]
        for i in range(1,len(prices)):
            m=max(m,prices[i]-r)
            r=min(prices[i],r)
        return m