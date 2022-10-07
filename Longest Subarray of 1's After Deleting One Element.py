class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,k,m=0,0,0,0
        while r<len(nums):
            if nums[r]==0:
                k-=1
            while k==-1:
                m=max(m,r-l)
                if nums[l]==0:
                    k+=1
                l+=1
            m=max(r-l+1,m)
            r+=1
        return m-1
