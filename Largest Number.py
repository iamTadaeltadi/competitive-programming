class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        s=list(map(str,nums))
        for g in range(len(nums)):
            r=g+1
            for j in range(r,len(nums)):
                if s[g]+s[j]<s[j]+s[g]:
                    s[g],s[j]=s[j],s[g]
                else:pass
        return str(int("".join(s)))
                
                
                
            
            
