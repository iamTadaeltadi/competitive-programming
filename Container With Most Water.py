class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        t=len(h)-1
        m=0
        while l<r:
            if h[l] <=h[r]:
                m=max(m,h[l]*t)
                l+=1
            else:
                h[l] >=h[r]
                m=max(m,h[r]*t)
                r-=1
            t-=1
        return m
       
