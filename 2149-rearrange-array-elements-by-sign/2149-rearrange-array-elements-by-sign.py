class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        for i in range(len(nums)):
            if nums[i] <0:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        l=0
        r=0
        while l<len(nums)//2:
            nums[r]=even[l]
            nums[r+1]=odd[l]
            l+=1
            r+=2
        return nums
        
    
                
                
        