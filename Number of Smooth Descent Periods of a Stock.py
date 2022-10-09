class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l=0
        m=0
        print(len(prices))
        for r in range(1,len(prices)):
            if prices[r-1]-prices[r]==1:
                pass
            else:
                if r>l+1:
                    m+=((len(prices[l:r]))*(len(prices[l:r])+1))//2-(r-l)
                l=r
            if r==len(prices)-1:
                if prices[r-1]-prices[r]==1:
                     m+=((len(prices[l:r+1]))*(len(prices[l:r+1])+1))//2-(r-l+1)
        m+=len(prices)
        return m
            
            
            
        
