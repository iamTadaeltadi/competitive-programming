class Solution:
    def maxVowels(self, nums: str, k: int) -> int:
        x={"a","e","i","o","u"}
        c=0
        l,r=0,k-1
        for i in nums[:k]:
            if i in x:
                c+=1
        m=c
        while r<len(nums)-1:
            if nums[r+1] in x:
                c+=1
            if nums[l] in x:
                c-=1
            r+=1
            l+=1
            m=max(m,c)
        return m
            

            
            
        
