class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split() 
        g=[0]*len(x)
        for i in x:
            g[int(i[-1])-1]=i[:-1]
        return " ".join(g)
