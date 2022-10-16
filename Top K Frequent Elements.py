class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        def getkey(v):
            for i in d.keys():
                if d[i]==v:
                    del d[i]
                    return i

        c=list(d.values())
        c.sort()
        x=[]
        for i in range(k):
            x.append(getkey(c.pop()))
        
        return x
            
