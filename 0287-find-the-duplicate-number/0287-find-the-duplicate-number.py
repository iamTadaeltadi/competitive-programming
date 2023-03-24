class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            
            while i+1!=nums[i] and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if i+1!=nums[i]:
                res=nums[i]
        return res