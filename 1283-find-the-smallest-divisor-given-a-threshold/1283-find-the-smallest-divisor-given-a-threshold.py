class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=low+(high-low)//2
            tot=0
            for i in nums:
                if i%mid==0:
                    tot+=i//mid
                else:
                    tot+=i//mid + 1
            if tot>threshold:
                low=mid+1
            else:
                high=mid-1
    
        return low
    
    