class Solution:
    def balancedString(self, s: str) -> int:
        count=Counter(s)
        n=len(s)
        sett=set()
        l=0
        m=float("inf")
        print(count)
        for i in count:
            print(count[i],n/4)
            if count[i]>n/4:
                count[i]-=n/4
                
                sett.add(i)
            else:
                 count[i]=0
            
        if not sett:return 0
        
        for r  in range(n):
            if s[r] in sett:
                count[s[r]]-=1
            while max(count.values())<=0:
                m=min(m,r-l+1)
                if s[l] in sett:
                    count[s[l]]+=1
                l+=1
                
        return m
            
                
            
       