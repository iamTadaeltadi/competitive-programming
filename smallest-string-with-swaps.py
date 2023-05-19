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

        repx=(self.find(x))
        repy=(self.find(y))
    
        self.rep[repx]=repy
       
            
    
    def isconnected(self,x,y):
          return  self.find(x)==self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        Dis=Disjoint(len(s))
        ans=[]
        graph=defaultdict(lambda:([],[]))
        print(graph)

        for i,j in pairs:
            Dis.union(i,j)

        for i,char in enumerate(s):
            parent=Dis.find(i)
            graph[parent][0].append(i)
            graph[parent][1].append(char)
        res = [''] * len(s)
        for ids, chars in graph.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)