class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid =low +(high-low)//2
            d=1
            tot=0
            for i in weights:
                tot+=i
                if mid<tot:
                    tot=i
                    d+=1
                
           
            if days >=d:
                high=mid-1
                
            else: 
                
                low=mid+1
       
        return low
   
        
        