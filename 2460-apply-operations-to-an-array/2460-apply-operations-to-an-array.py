class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        r=1
        l=0
        while r<len(nums):
            if nums[l]==0:
                while r<len(nums)-1 and nums[r]==0:
                    r+=1
                nums[l],nums[r]=nums[r],nums[l]
            r+=1
            l+=1
        return nums
            
                
        