class Solution:
    def countPalindromicSubsequence(self, nums: str) -> int:
        d=defaultdict(list)
        for i,j in enumerate(nums):
            d[j].append(i)
        res=0
        for i in d.keys():
            if len(d[i])>1 and d[i][-1]-d[i][0]>1:
                a=set(nums[d[i][0]+1:d[i][-1]]) 
                res+=len(a)
        return res
                
                
        
            
        
            
            
            