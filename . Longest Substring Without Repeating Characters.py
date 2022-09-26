class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        l,r=0,1
        m=1
        x=[]
        if not nums:return 0
        c=[nums[0]]
        while r<len(nums):
            if nums[r] in c[l:]:
                x.append(len(c[l:]))
                l+=1
            else:
                c.append(nums[r])
                x.append(len(c[l:]))
                r+=1
        if not x:return m
        return max(x)
