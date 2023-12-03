class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=0
        d={}
        x=[]
        for i in range(10,len(s)+1):
            if s[l:i] not in d:
                d[s[l:i]]=0
            d[s[l:i]]+=1
            l+=1
        print(d)
        for i in d:
            if d[i] >=2:
                x.append(i)
        return x
            
            
        