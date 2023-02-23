class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tot=0
        c=0
        l=0
        n=len(nums)
        res=0
        count=0
        for r in range(n):
            tot+=nums[r]
            res=tot*(r-l+1)
            while res>=k:
                tot-=nums[l]
                l+=1
                res=tot*(r-l+1)
            count+=r-l+1
      
        return count
            
            
        