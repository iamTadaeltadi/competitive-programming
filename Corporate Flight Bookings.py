class Solution:
    def corpFlightBookings(self, nums: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n+1)
        count=0
        for i in nums:
            start,end,seat=i
            arr[start-1]+=seat
            arr[end]-=seat
        for i,num in enumerate(arr):
            count+=num
            arr[i]=count
        return arr[:n]
