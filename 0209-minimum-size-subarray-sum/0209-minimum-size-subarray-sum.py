class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n=len(nums)
        tot=0
        l=0
        m=n
        flag=False
        for r in range(n):
            tot+=nums[r]
            while tot >= target:
                flag=True
                m=min(m,r-l+1)
                tot-=nums[l]
                l+=1
        if (not flag) and m==n:
            return  0
        
        return m
        