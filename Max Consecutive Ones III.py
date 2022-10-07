class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r,m=0,0
        while r<len(nums):
            if nums[r]==0:
                k-=1
            while k==-1:
                m=max(m,r-l)
                if nums[l]==0:
                    k+=1
                l+=1
            m=max(m,r-l+1)
            r+=1
        return m
