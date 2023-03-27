class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]>n or nums[i]<0:
                nums[i]=0
        for i in range(len(nums)):
            while nums[i]!=0 and nums[i]!=i+1:
                if nums[i]==nums[nums[i]-1]:
                    nums[max(i,nums[i]-1)]=0
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                
        for i in range(n):
            if nums[i]==0:
                return i+1
        return n+1