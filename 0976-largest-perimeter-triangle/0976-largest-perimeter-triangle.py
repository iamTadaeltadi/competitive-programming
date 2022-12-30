class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        r=2
        summ=0
        maxx=0
        while r<len(nums):
            if (nums[r])<(nums[r-1])+(nums[l]):
                summ=sum(nums[l:r+1])
            maxx=max(summ,maxx)
            r+=1
            l+=1
        return maxx
                
            
    
    