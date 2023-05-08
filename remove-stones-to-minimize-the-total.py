class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #i need max heap cause to maximum every k operation
         
        piles=[-1*i for i in piles]
        heapq.heapify(piles)
        
        while k>0:
            maxVal=-1*heapq.heappop(piles)
            

            heapq.heappush(piles,-1*math.ceil(maxVal/2))
            k-=1
        
        return -1*sum(piles)