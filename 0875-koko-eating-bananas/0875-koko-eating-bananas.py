class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid =low +(high-low)//2
            hours=0
            for i in piles:
                if mid>=i:
                    hours+=1
                else:
                    hours+=(i//mid)
                    if i % mid != 0:
                        hours += 1
            print(mid,hours)
            if hours >h:
                low=mid+1
            elif hours <=h:
                high=mid-1
            else:
                return mid
        return low 
        
        