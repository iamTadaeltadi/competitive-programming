class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        count=Counter(s1)
        current=Counter(s2[:r-1])
        print(current,count)

        
        for right in range(r-1,len(s2)):
            current[s2[right]]=current.get(s2[right],0) + 1
            
            if current==count:
                return True
            current[s2[l]]-=1
            if current[s2[l]]==0:
                del current[s2[l]]
            l+=1
            
        return False
            
            
            
            
        
