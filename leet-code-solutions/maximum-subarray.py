class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=nums[0]
        c=0
        for i in nums:
            if c<0:
                c=0
            c+=i
            ma=max(ma,c)
        return ma
            
    