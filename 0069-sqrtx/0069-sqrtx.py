class Solution:
    def mySqrt(self, x: int) -> int:
        high=x
        low=0
        while low <=high:
            mid=low +(high-low)//2
            val=mid**2
            if val>x:
                high=mid-1
            elif val<x:
                low=mid+1
            else:
                
                return mid
        return low-1
            