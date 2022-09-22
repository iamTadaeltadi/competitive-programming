class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        d={0:"M",1:"P",2:"G"}
        v=0
        m=[len(garbage[0])]
        for i in range(1,len(garbage)):
            m.append(m[-1]+len(garbage[i]))
        print(m)
        g=''.join(garbage)         
        for i in range(len(garbage)):
            l=len(garbage[i])
            x=0
            c=0
            for j in range(3):
                if d[x] in g[m[i]:]:
                    c+=1
                x+=1
            if i<len(garbage)-1:
                v+=l+c*travel[i]
            else:
                v+=l
        return v
            
