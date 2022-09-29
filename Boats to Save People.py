class Solution:
    def numRescueBoats(self, p: List[int], li: int) -> int:
        p.sort()
        l,t=0,0
        r=len(p)-1
        while l <=r:
            if p[r]<li:
                if p[r]+p[l]<=li:
                    r-=1
                    l+=1
                else:
                    r-=1
            else:
                r-=1
            t+=1
        return t
            
            
            
