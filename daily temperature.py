class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while s and s[-1][0]<t:
                st,si=s.pop()
                res[si]=i-si
            s.append([t,i])
        return res
                
            
