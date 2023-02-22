class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=Counter(p)
        res=[]
        nn=len(p)
        x=Counter(s[:len(p)-1])
        for i in range(len(s)-nn+1):
            if s[i+nn-1] in x:
                x[s[i+nn-1]]+=1
            else:
                x[s[i+nn-1]]=1
            if x==n:
                res.append(i)
            x[s[i]]-=1
            if x[s[i]]==0:
                del x[s[i]]
            
            
        return res
        
                
                
            
            
            
            
            