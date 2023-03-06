class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        if not nums:
            return [-1,-1]
        
        while low<=high:
            mid=low +(high-low)//2
            if nums[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        start_index=low
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low +(high-low)//2
            if nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        last_index=low-1
        print(start_index)
        if start_index>=len(nums)or nums[start_index]!=target:
            return [-1,-1]
            
        return [start_index,last_index]
        
        