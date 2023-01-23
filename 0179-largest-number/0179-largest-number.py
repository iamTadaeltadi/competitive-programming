class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        nums.sort()
        nums=list(map(str,nums))
        print(nums)
        for _ in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]> nums[i+1]+nums[i]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        
        return str(int("".join(nums[::-1])))
                
            
        
            
            