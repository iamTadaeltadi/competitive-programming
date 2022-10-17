class Solution:
    def bagOfTokensScore(self, nums: List[int], power: int) -> int:
        nums.sort()
        l,s,m=0,0,0
        r=len(nums)-1
        while l<=r:
            if nums[l]>power and s>=1:
                power+=nums[r]
                r-=1
                s-=1
            elif nums[l]<=power:
                power-=nums[l]
                l+=1
                s+=1
            else:return 0
            m=max(m,s)
        return m
