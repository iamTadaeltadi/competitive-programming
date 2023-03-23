class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        minVal = min(nums)
        rangee = maxVal-minVal+1
        kk = 0
        count = [0]*rangee
        
        for index in range(len(nums)):
            count [nums[index]-minVal] +=1
            
        c=0
        for i in range(len(count)-1,-1,-1):
            kk += count[i]
            if kk >=k:
                return (maxVal-c)
            c+=1
        return 2
            
        