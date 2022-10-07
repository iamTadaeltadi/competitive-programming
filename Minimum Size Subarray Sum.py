class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        l,to=0,0
        m=float("inf")
        for i in range(len(nums)):
            to+=nums[i]
            while to>=t:
                to-=nums[l]
                m=min(m,i-l+1)
                l+=1
        if m==float("inf"):
            return 0
        return m
                
