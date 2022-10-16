class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        d=Counter(arr)
        dd=list(d.values())
        dd.sort()
        n=len(arr)//2
        c=1
        t=dd[-1]
        for i in range(len(dd)-1,0,-1):
            if t>=n:
                return c
            else:
                t+=dd[i-1]
                c+=1
        return c
        
