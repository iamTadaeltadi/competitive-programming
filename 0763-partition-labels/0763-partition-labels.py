class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count=Counter(s)
        curr={}
        res=[]
        left=0
        
        for right in range(len(s)):
            count[s[right]]-=1
            curr[s[right]]=count[s[right]]
            
            if (all(item == 0 for item in curr.values())):
                res.append(right-left+1)
                left=right+1
                
        return res
            
                
            
        
            