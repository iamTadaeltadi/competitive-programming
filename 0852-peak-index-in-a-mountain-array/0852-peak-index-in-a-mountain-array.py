class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        high=len(arr)-2
        low=1
        def rec(low,high):
            mid =low +(high-low)//2
            if arr[mid]>arr[mid-1] and arr[mid] >arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid-1]:
                return rec(low,mid-1)
            else:
                 return rec(mid+1,high)
        return rec(low,high)
                
                
        