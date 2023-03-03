class Solution:
    def mySqrt(self, x: int) -> int:
        
        def rec(high,low):
            mid=low +(high-low)//2
            val=mid**2
        
            if low >high:
                return low-1
            if val>x:
                return rec(mid-1,low)
            elif val<x:
                return rec(high,mid+1)
            else:
                return mid
        return rec(x,0)
        
            