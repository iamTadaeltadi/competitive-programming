class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        l=[]
        c=0
        for i,j in points:
            l.append([points[c], math.sqrt(i ** 2 + j ** 2)])
            c += 1
        l.sort(key=lambda x:x[1])
        x=[]
        for i in range(k):
            x.append(l[i][0])
    
        return x
