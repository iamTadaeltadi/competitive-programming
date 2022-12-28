class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=sum(nums)
        
        n=len(nums)
        sum_org=((n+1)*n)/2
        return sum_org-summ
        
            
            
      
            