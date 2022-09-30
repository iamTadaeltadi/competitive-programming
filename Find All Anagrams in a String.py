class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        r=len(p)-1
        y=Counter(p)
        z=[]
        x=Counter(s[l:r+1])
        if len(p)==len(s):
            r-=1
        while r<len(s)-1:
           
            if x==y:
                z.append(l)
            if s[r+1] not in x:
                x[s[l]]-=1
                if s[r+1] not in x:
                    x[s[r+1]]=0
                x[s[r+1]]+=1
            elif s[r+1] in x:
                x[s[r+1]]+=1
                x[s[l]]-=1
            if r==len(s)-2:
                if x==y:
                    z.append(l+1)
            r+=1
            l+=1
        return z
    
                    
                    
                
                    
                    
