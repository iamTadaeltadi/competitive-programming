class Disjoint():
    def __init__(self,n):
        self.rep=[ i for i in range(n)]
        self.rank=[inf for i in range(n)]
    

    def find(self,x):
        if self.rep[x]==x:
            return x

        the_rep=self.find(self.rep[x])
        self.rep[x]=the_rep
        return the_rep
    def union(self,x,y):
        repx=self.find(x)
        repy=self.find(y)
       
        if repx>repy:
            self.rep[repx]=repy
            
        else:
            self.rep[repy]=repx
            
    
    def isconnected(self,x,y):
          return  self.find(x)==self.find(y)





class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        Dis=Disjoint((26))
        ans=[]
        graph=defaultdict(list)
        for i in range(len(s1)):
            graph[s1[i]].append(s2[i])
            graph[s2[i]].append(s2[i])
            Dis.union(ord(s1[i])-97,ord(s2[i])-97)
        for i in baseStr:
            ans.append(chr(Dis.find(ord(i)-97)+97))
            
        return "".join(ans)
    
            

            
            
        
        